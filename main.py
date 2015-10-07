import EdgeDetection
from PIL import Image, ImageDraw
import KernelsDictionary

filterName = input('mode(sobel, previt):')
ImageAddrass = input('image:')
image = Image.open(ImageAddrass)
kernel = KernelsDictionary.edgeDetection_Dict[filterName]
EdgeDetection.process(image, kernel[0], kernel[1])
image.save('edgeDetection.jpg', "JPEG")
