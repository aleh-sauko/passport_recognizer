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

class MatrixFilter(AbstractFilter):
  """Matrix Abstract Filter"""

  def __processPixel(self, kernel, i, j):
    r, g, b = 0, 0, 0
    (kernelWidth, kernelHeight) = kernel.shape
    for (cc, rr), k in np.ndenumerate(kernel):
      posX = i + (cc - kernelWidth//2)
      posY = j + (rr - kernelHeight//2)
      if not (0 <= posX < self.width) or not (0 <= posY < self.height): 
        continue
      r += self.pixels[posX, posY][0] * k
      g += self.pixels[posX, posY][1] * k
      b += self.pixels[posX, posY][2] * k
    return self._bound_pixel((r, g, b))

  BLUR = "BLUR"
  BLUR5 = "BLUR5"
  CLARIFY = "CLARIFY"
  NOIZE = "NOIZE"
  EDGES = "EDGES"

  """ Supported Matrix filters """
  predefined_filters_set = set([BLUR, BLUR5, NOIZE, CLARIFY, EDGES])

  BLUR_KERNEL = np.array([[1.,2,1],[2,4,2],[1,2,1]])
  BLUR5_KERNEL = np.array([[1.,4,7,4,1], [4,16,26,16,4], [7,26,41,26,7], [1,4,7,4,1], [4,16,26,16,4]])
  CLARIFY_KERNEL = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
  NOIZE_KERNEL = np.array([[1,1,1],[1,1,1],[1,1,1]])
  EDGES_KERNEL = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

  """ Dispatcher of kernels """
  __kernel_dispatcher = {
    BLUR: BLUR_KERNEL,
    BLUR5: BLUR5_KERNEL,
    CLARIFY: CLARIFY_KERNEL,
    NOIZE: NOIZE_KERNEL,
    EDGES: EDGES_KERNEL
  }


  def applyMatrix(self, filter_type, args=None):
    if filter_type in self.predefined_filter_set: 
      kernel = self.normalize(self.__kernel_dispatcher.get(filter_type))
    else:
      kernel = args
    for i in range(self.width):
      for j in range(self.height):
        self.draw.point((i, j), self.__processPixel(kernel, i, j)) 
    return self
