from PIL import Image, ImageDraw
import numpy as np 

from abc import ABCMeta, abstractmethod

class AbstractFilter(object):
  """Abstract Filter class"""

  __metaclass__ = ABCMeta

  def __init__(self, image):
    self.image = image
    self.width, self.height = image.size
    self.pixels = image.load()
    self.draw = ImageDraw.Draw(image)

  @staticmethod
  def normalize(matrix):
    sum = np.sum(matrix)
    if sum > 0.:
      return matrix / sum
    else:
      return matrix 

  @staticmethod
  def _bounded(x):
    if (x > 255): x = 255
    if (x < 0): x = 0
    return int(x)

  @staticmethod
  def _bound_pixel(pix):
    return (AbstractFilter._bounded(pix[0]), AbstractFilter._bounded(pix[1]), AbstractFilter._bounded(pix[2]))

  @staticmethod
  def build_gauss_kernel(sigma, radius):
    size = radius * 2 + 1
    coeff  = 1 / (2 * math.pi * sigma * sigma)
    down   = 2 * sigma * sigma
    kernel = np.zeros((size, size))

    for i in range(-radius, radius + 1):
      for j in range(-radius, radius + 1):
        up = math.pow(i, 2) + math.pow(j, 2)
        kernel[i + radius, j + radius] = coeff * math.exp(- up / down)
    return kernel

  @abstractmethod
  def apply(self):
    """Apply Filter"""
    pass