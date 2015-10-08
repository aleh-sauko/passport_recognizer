import numpy as np 
from PIL import Image, ImageDraw
import sys
import convolve
import median
				
kernel_blur = np.array([[1.,2,1],[2,4,2],[1,2,1]])
kernel_blur5 = np.array([[1.,4,7,4,1],
												[4,16,26,16,4],
												[7,26,41,26,7],
												[1.,4,7,4,1],
												[4,16,26,16,4]])
kernel_clarify = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
kernel_noize = np.array([[1,1,1],[1,1,1],[1,1,1]])
kernel_dictionary = { 'blur': kernel_blur, 'blur5': kernel_blur5, 'clarify': kernel_clarify, 'noize': kernel_noize }


image = Image.open(sys.argv[1])

kernel = kernel_blur
if (len(sys.argv) > 2 and sys.argv[2] in kernel_dictionary):
	kernel = kernel_dictionary[sys.argv[2]]
	print ('Kernel: ' + str(kernel))
	convolve.process(image, kernel)
elif sys.argv[2] == 'median':
	median.process(image, int(sys.argv[3]))

image.save("res.png", "png")

