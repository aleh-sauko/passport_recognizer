''' 
  For Testing Purpose! 
  Hack, with which we can compile file like a standalone file and like a package!
'''
if __name__ == '__main__' and __package__ is None:
  from os import sys, path
  sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
  from abstract_filter import AbstractFilter
else:
  from ..abstract_filter import AbstractFilter

from PIL import Image, ImageDraw
import numpy as np 
import math

class LinearFilter(AbstractFilter):

  """ Simple Linear Filters """

  def __grey_filter(self):
    for i in range(self.width):
      for j in range(self.height):
        r = self.pixels[i, j][0]
        g = self.pixels[i, j][1]
        b = self.pixels[i, j][2]
        s = (r + g + b) // 3
        self.draw.point((i, j), (int(s), int(s), int(s)))
    return self

  def __negative_filter(self):
    for i in range(self.width):
      for j in range(self.height):
        r = 255 - self.pixels[i, j][0]
        g = 255 - self.pixels[i, j][1]
        b = 255 - self.pixels[i, j][2]
        self.draw.point((i, j), (int(r), int(g), int(b)))
    return self

  def __black_and_white_filter(self, factor):
    for i in range(self.width):
      for j in range(self.height):
        r = self.pixels[i, j][0]
        g = self.pixels[i, j][1]
        b = self.pixels[i, j][2]
        s = r + g + b
        if s > (( 255 + factor) // 2) * 3:
          r, g, b = 255, 255, 255
        else:
          r, g, b = 0, 0, 0
        self.draw.point((i, j), (int(r), int(g), int(b)))
    return self

  def __bright_filter(self, factor):
    for i in range(self.width):
      for j in range(self.height):
        r = factor * math.log(1 + self.pixels[i, j][0])
        g = factor * math.log(1 + self.pixels[i, j][1])
        b = factor * math.log(1 + self.pixels[i, j][2])
        self.draw.point((i, j), (int(r), int(g), int(b)))
    return self

  # TODO: Put in another module
  def __median_filter(self, factor):
    for i in range(self.width):
      for j in range(self.height):
        vals = []
        for x in range(i-factor//2, i+factor//2+1):
          for y in range(j-factor//2, j+factor//2+1):
            c, r = x, y
            if (y < 0): r = 0
            if (x < 0): c = 0
            if (y >= self.height): r = self.height - 1    
            if (x >= self.width): c = self.width - 1  
            vals.append(self.pixels[c,r][0]*(256**2)+self.pixels[c,r][1]*256+self.pixels[c,r][2])
        vals = np.sort(vals)  
        val = vals[len(vals)//2]
        r = val // (256**2)
        val -= r * (256**2)
        g = val // 256
        b = val % 256
        self.draw.point((i, j), (r, g, b))
    return self

  GREY = "GREY"
  NEGATIVE = "NEGATIVE"
  BLACK_AND_WHITE = "BLACK_AND_WHITE"
  BRIGHT = "BRIGHT"
  MEDIAN = "MEDIAN"

  """ Supported Linear filters """
  predefined_filters_set = set([GREY, NEGATIVE, BRIGHT, BLACK_AND_WHITE, MEDIAN])


  """ Dispatcher of filters """
  __filter_dispatcher_without_params = {
    GREY: __grey_filter,
    NEGATIVE: __negative_filter
  }

  __filter_dispatcher_with_params = {
    BRIGHT: __bright_filter,
    BLACK_AND_WHITE: __black_and_white_filter,
    MEDIAN: __median_filter
  }

  def applyLinear(self, filter_type, arg=None):
    if arg is None:
      return self.__filter_dispatcher_without_params.get(filter_type, lambda x: "filter not founded or given without args")(self)
    else: 
      return self.__filter_dispatcher_with_params.get(filter_type, lambda x: "filter not founded")(self, arg)
