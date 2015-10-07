import numpy as np
from MatrixFilter import getKernelDiv, bound, bordersCorrect, doConvolution
from PIL import Image, ImageDraw
import math



def getGradient(d1, d2):
	return math.sqrt(math.pow(d1,2) + math.pow(d2,2))

def filter(original, result, kernelFst, kernelSnd, size):
	kSize = kernelFst.shape
	for row in range(size[0]):
		for col in range(size[1]):
			top = row - kSize[0]//2
			bottom = row + kSize[0]//2 + 1
			left = col - kSize[1]//2
			right = col + kSize[1]//2 + 1
			if not bordersCorrect(size, top, bottom, left, right): continue

			section = original[top:bottom, left:right]
			d1 = doConvolution(section, kernelFst, kSize)
			d2 = doConvolution(section, kernelSnd, kSize)

			r = getGradient(d1[0], d2[0])
			g = getGradient(d1[1], d2[1])
			b = getGradient(d1[2], d2[2])

			result.point((col, row), (bound(r), bound(g), bound(b)))
			

def process(image, kernelFst, kernelSnd):
	width = image.size[0]
	height = image.size[1]
	originalArr = np.array(image)
	draw = ImageDraw.Draw(image)
	filter(originalArr, draw, kernelFst, kernelSnd, (height, width))
	




