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

from .matrix_filters import MatrixFilter
from PIL import Image, ImageDraw
import numpy as np
import math


class EdgeDetectionFilter(AbstractFilter):

  SOBEL_KERNEL = np.array([[[-1,-2,-1],[0,0,0],[1,2,1]],
                          [[-1,0,1],[-2,0,2],[-1,0,1]]])

  PREVIT_KERNEL = np.array([[[-1,-1,-1],[0,0,0],[1,1,1]],
                            [[-1,0,1],[-1,0,1],[-1,0,1]]])

  SOBEL = "SOBEL"
  PREVIT = "PREVIT"

  predefined_filters_set = set([SOBEL, PREVIT])

  """ Dispatcher of kernels """
  __kernel_dispatcher = {
    SOBEL: SOBEL_KERNEL,
    PREVIT: PREVIT_KERNEL
  }

  @staticmethod
  def __get_gradient(d1, d2):
    return math.sqrt(math.pow(d1,2) + math.pow(d2,2))

  @staticmethod
  def __get_gradient_from_pixels(a, b):
    return (EdgeDetectionFilter.__get_gradient(a[0], b[0]), 
            EdgeDetectionFilter.__get_gradient(a[1], b[1]), 
            EdgeDetectionFilter.__get_gradient(a[2],b[2]))

  def __proccess_pixel(self, posX, posY, kernels):
    r1, g1, b1 = 0,0,0
    r2, g2, b2 = 0,0,0
    kernels[0] = self.normalize(kernels[0])
    kernels[1] = self.normalize(kernels[1])

    (k_width, k_height) = kernels[0].shape
    for (cc, rr), v in np.ndenumerate(kernels[0]):
      i = posX + (cc - k_width//2)
      j = posY + (rr - k_height//2)

      r1 += (self.pixels[i,j][0] * kernels[0][cc,rr])
      g1 += (self.pixels[i,j][1] * kernels[0][cc,rr]) 
      b1 += (self.pixels[i,j][2] * kernels[0][cc,rr])

      r2 += (self.pixels[i,j][0] * kernels[1][cc,rr]) 
      g2 += (self.pixels[i,j][1] * kernels[1][cc,rr]) 
      b2 += (self.pixels[i,j][2] * kernels[1][cc,rr])  
    return self._bound_pixel(self.__get_gradient_from_pixels(
                              self._bound_pixel((r1, g1, b1)), 
                              self._bound_pixel((r2, g2, b2))))

  def __borders_correct(self, left, right, top, bottom):
    if not (0 <= left < self.width) or not (0 <= right < self.width):
      return False
    if not (0 <= top < self.height) or not (0 <= bottom < self.height):
      return False
    return True

  def applyEdgeDetection(self, filter_type, args=None):
    kernels = self.__kernel_dispatcher.get(filter_type)
    (k_width, k_height) = kernels[0].shape
    for i in range(self.width):
      for j in range(self.height):
        left = i - k_width//2
        right = i + k_height//2 + 1
        top = j - k_height//2
        bottom = j + k_height//2 + 1
        if not self.__borders_correct(left, right, top, bottom): continue

        resultPix = self.__proccess_pixel(i, j, kernels)
        self.draw.point((i, j), resultPix)    
    return self



