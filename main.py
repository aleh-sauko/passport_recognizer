from filters.filter import *
import numpy as np
from PIL import Image, ImageDraw
import sys

image = Image.open('source_images/dark_image.jpg')
Filter(image).applyLinear(LinearFilter.BRIGHT, 40).applyEdgeDetection(EdgeDetectionFilter.SOBEL)#.applyLinear(LinearFilter.BLACK_AND_WHITE, 20)
image.show()