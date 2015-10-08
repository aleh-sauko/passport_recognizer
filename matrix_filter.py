import numpy as np
from PIL import Image, ImageDraw

def get_kernel_div(kernel):
	div = np.sum(kernel)
	if div <= 0 : div = 1
	return div

def bound(x):
	if x < 0 : x = 0
	elif x > 255 : x = 255
	return int(x)

def bound_pixel(pix):
	return (bound(pix[0]), bound(pix[1]), bound(pix[2]))

def borders_correct(size, t, b, l, r):
	if t < 0 or l < 0 or (b > size[0]) or (r > size[1]):
		return False
	else: return True

def convolve(section, kernel, size):
	r, g, b = 0, 0, 0
	div = get_kernel_div(kernel)

	for i in range(size[0]):
		for j in range(size[1]):
			r += (section[i,j][0] * kernel[i,j])//div 
			g += (section[i,j][1] * kernel[i,j])//div 
			b += (section[i,j][2] * kernel[i,j])//div 
	return bound_pixel((r,g,b))

def filter(original, result, kernel, size):
	kSize = kernel.shape
	for row in range(size[0]):
		for col in range(size[1]):
			top = row - kSize[0]//2
			bottom = row + kSize[0]//2 + 1
			left = col - kSize[1]//2
			right = col + kSize[1]//2 + 1
			if not borders_correct(size, top, bottom, left, right): continue

			section = original[top:bottom, left:right]
			rgb = convolve(section, kernel, kSize)
			result.point((col, row), (rgb[0], rgb[1], rgb[2]))

def process(image, kernel):
	width = image.size[0]
	height = image.size[1]
	original = np.array(image)
	draw = ImageDraw.Draw(image)
	filter(original, draw, kernel, (height, width))
