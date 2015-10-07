import EdgeDetection
from PIL import Image, ImageDraw
import KernelsDictionary
import MatrixFilter

filterName = input('mode(sobel, previt):')
ImageAddrass = input('image:')
image = Image.open(ImageAddrass)
kernel = KernelsDictionary.kernel_Dict[filterName]
MatrixFilter.process(image, kernel)
image.save('clarify.jpg', "JPEG")
