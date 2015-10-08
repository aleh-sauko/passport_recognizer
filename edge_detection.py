import numpy as np
from matrix_filter import get_kernel_div, bound_pixel, borders_correct
from PIL import Image, ImageDraw
import math

def get_gradient(d1, d2):
	return math.sqrt(math.pow(d1,2) + math.pow(d2,2))

def get_gradient_from_pixels(a, b):
	return (getGradient(a[0], b[0]), getGradient(a[1], b[1]), getGradient(a[2],b[2]))


def normalize_pix(pix, div):
	return (pix[0]//div, pix[1]//div, pix[2]//div)

def convolve(section, kernels, size):
	r1, g1, b1 = 0,0,0
	r2, g2, b2 = 0,0,0
	div1 = get_kernel_div(kernels[0])
	div2 = get_kernel_div(kernels[1])

	for i in range(size[0]):
		for j in range(size[1]):
			r1 += (section[i,j][0] * kernels[0][i,j])
			g1 += (section[i,j][1] * kernels[0][i,j]) 
			b1 += (section[i,j][2] * kernels[0][i,j])

			r2 += (section[i,j][0] * kernels[1][i,j]) 
			g2 += (section[i,j][1] * kernels[1][i,j]) 
			b2 += (section[i,j][2] * kernels[1][i,j])  

	pix1 = normalize_pix((r1, g1, b1), div1)
	pix2 = normalize_pix((r2, g2, b2), div2)

	pix1 = bound_pixel(pix1)
	pix2 = bound_pixel(pix2)

	rgbResult = get_gradient_from_pixels(pix1, pix2)
	return bound_pixel(rgbResult)

def filter(original, result, kernels, size):
	kSize = kernels[0].shape
	for row in range(size[0]):
		for col in range(size[1]):
			top = row - kSize[0]//2
			bottom = row + kSize[0]//2 + 1
			left = col - kSize[1]//2
			right = col + kSize[1]//2 + 1
			if not borders_correct(size, top, bottom, left, right): continue

			section = original[top:bottom, left:right]
			resultPix = convolve(section, kernels, kSize)
			result.point((col, row), resultPix)
			

def process(image, kernels):
	width = image.size[0]
	height = image.size[1]
	originalArr = np.array(image)
	draw = ImageDraw.Draw(image)
	filter(originalArr, draw, kernels, (height, width))
	




