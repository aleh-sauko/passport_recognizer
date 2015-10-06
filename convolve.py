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

def processPixel(width, height, pix, i, j, kernel):
	kernel = normalize(kernel)
	r, g, b = 0, 0, 0
	(kernelWidth, kernelHeight) = kernel.shape
	for (cc,rr), k in np.ndenumerate(kernel):
		posX = i + (cc - kernelWidth//2)			
		posY = j + (rr - kernelHeight//2)
		if not (0 <= posX < width) or not (0 <= posY < height): 
			continue
		r += pix[posX, posY][0] * k
		g += pix[posX, posY][1] * k
		b += pix[posX, posY][2] * k
	return (bounded(r), bounded(g), bounded(b))

def process(image, kernel):
	width, height = image.size
	pix = image.load()
	draw = ImageDraw.Draw(image)
	for i in range(width):
		for j in range(height):
			draw.point((i, j), processPixel(width, height, pix, i, j, kernel))
	return image


