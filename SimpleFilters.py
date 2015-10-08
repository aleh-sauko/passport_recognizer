from PIL import Image, ImageDraw
import numpy as np

def makeGray(image):
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S=(a+b+c) // 3
			draw.point((i,j),(S,S,S))


def makeNegative(image):
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			r = 255 - pix[i, j][0]
			g = 255 - pix[i, j][1]
			b = 255 - pix[i, j][2]
			draw.point((i,j),(r,g,b))

def makeBlackWhite(image, factor):
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			s = a+b+c
			if s>(( 255 + factor) // 2) * 3:
				a,b,c = 255,255,255
			else:
				a,b,c = 0,0,0
			draw.point((i,j),(a,b,c))

