import EdgeDetection
from PIL import Image, ImageDraw
import KernelsDictionary

filterName = input('mode(sobel, previt):')
ImageAddrass = input('image:')
image = Image.open(ImageAddrass)
kernel = KernelsDictionary.edgeDetection_Dict[filterName]
EdgeDetection.process(image, kernel)
image.save('edgeDetection.jpg', "JPEG")
