import numpy as np
from MatrixFilter import getKernelDiv, boundPixel, bordersCorrect
from PIL import Image, ImageDraw
import math

def getGradient(d1, d2):
	return math.sqrt(math.pow(d1,2) + math.pow(d2,2))

def getGradientFromPixels(a, b):
	return (getGradient(a[0], b[0]), getGradient(a[1], b[1]), getGradient(a[2],b[2]))


def normalizePix(pix, div):
	return (pix[0]//div, pix[1]//div, pix[2]//div)

def doConvolution(section, kernels, size):
	r1, g1, b1 = 0,0,0
	r2, g2, b2 = 0,0,0
	div1 = getKernelDiv(kernels[0])
	div2 = getKernelDiv(kernels[1])

	for i in range(size[0]):
		for j in range(size[1]):
			r1 += (section[i,j][0] * kernels[0][i,j])
			g1 += (section[i,j][1] * kernels[0][i,j]) 
			b1 += (section[i,j][2] * kernels[0][i,j])

			r2 += (section[i,j][0] * kernels[1][i,j]) 
			g2 += (section[i,j][1] * kernels[1][i,j]) 
			b2 += (section[i,j][2] * kernels[1][i,j])  

	pix1 = normalizePix((r1, g1, b1), div1)
	pix2 = normalizePix((r2, g2, b2), div2)

	pix1 = boundPixel(pix1)
	pix2 = boundPixel(pix2)

	rgbResult = getGradientFromPixels(pix1, pix2)
	return boundPixel(rgbResult)

def filter(original, result, kernels, size):
	kSize = kernels[0].shape
	for row in range(size[0]):
		for col in range(size[1]):
			top = row - kSize[0]//2
			bottom = row + kSize[0]//2 + 1
			left = col - kSize[1]//2
			right = col + kSize[1]//2 + 1
			if not bordersCorrect(size, top, bottom, left, right): continue

			section = original[top:bottom, left:right]
			resultPix = doConvolution(section, kernels, kSize)
			result.point((col, row), resultPix)
			

def process(image, kernels):
	width = image.size[0]
	height = image.size[1]
	originalArr = np.array(image)
	draw = ImageDraw.Draw(image)
	filter(originalArr, draw, kernels, (height, width))
	




