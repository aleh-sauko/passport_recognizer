import numpy as np 
from PIL import Image, ImageDraw

def normalize(matrix):
	sum = np.sum(matrix)
	if sum > 0.:
		return matrix / sum
	else:
		return matrix	

def bounded(x):
	if (x > 255): x = 255
	if (x < 0): x = 0
	return int(x)

def processPixel(height, width, pix, i, j, kernel):
	kernel = normalize(kernel)
	r, g, b = 0, 0, 0
	#height, width = pix.size[0], pix.size[1]
	(kernelHeight, kernelWidth) = kernel.shape
	for (r,c), k in np.ndenumerate(kernel):
		posY = i + (r - kernelHeight/2)
		posX = j + (c - kernelWidth/2)			
		if not (0 <= posX < width) or not (0 <= posY < height):
			continue
		r += pix[posY, posX][0] * k
		g += pix[posY, posX][1] * k
		b += pix[posY, posX][2] * k
	return (bounded(r), bounded(g), bounded(b))

def process(image, kernel):
	draw = ImageDraw.Draw(image)
	height = image.size[0]
	width = image.size[1]
	pix = image.load()
	for i in range(height):
		for j in range(width):
			draw.point((i, j), processPixel(height, width, pix, i, j, kernel))


