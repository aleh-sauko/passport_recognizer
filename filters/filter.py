''' 
  For Testing Purpose! 
  Hack, with which we can compile file like a standalone file and like a package!
'''
if __name__ == '__main__' and __package__ is None:
  from os import sys, path
  sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
  from linear_filters import LinearFilter
  from matrix_filters import MatrixFilter
  from matrix.edge_detection import EdgeDetectionFilter
else:
  from .linear.linear_filters import LinearFilter
  from .matrix.matrix_filters import MatrixFilter
  from .matrix.edge_detection import EdgeDetectionFilter

from PIL import Image, ImageDraw
import numpy as np 

class Filter(MatrixFilter, LinearFilter, EdgeDetectionFilter):

  """ Mixing of combining Matrix and Linear Filters """

  def apply(self, filter_type, args=None):
    if filter_type in LinearFilter.predefined_filters_set:
      self.applyLinear(filter_type, args)
    elif filter_type in MatrixFilter.predefined_filters_set:
      self.applyMatrix(filter_type, args)
    elif filter_type in EdgeDetectionFilter.predefined_filters_set:
      self.applyEdgeDetection(filter_type, args)
    return self

if __name__ == "__main__":
  image = Image.open('source_images/04.jpg')
  # MatrixFilter(image).apply(MatrixFilter.BLUR).apply(MatrixFilter.CLARIFY)
  Filter(image).applyEdgeDetection(EdgeDetectionFilter.PREVIT).applyLinear(LinearFilter.BLACK_AND_WHITE, 20)
  # Filter(image).apply(LinearFilter.MEDIAN, 2).apply(MatrixFilter.BLUR)
  image.show()