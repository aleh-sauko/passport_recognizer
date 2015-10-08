from PIL import Image, ImageDraw
import numpy as np

def make_gray(pixels, width, height):
	for i in range(width):
		for j in range(height):
			a = pixels[i, j][0]
			b = pixels[i, j][1]
			c = pixels[i, j][2]
			s =(a+b+c) // 3
			pixels[i, j] = (s, s, s)


def make_negative(pixels, width, height):
	for i in range(width):
		for j in range(height):
			r = 255 - pixels[i, j][0]
			g = 255 - pixels[i, j][1]
			b = 255 - pixels[i, j][2]
			pixels[i, j] = (r, g, b)

def make_black_white(pixels, width, height, factor):
	for i in range(width):
		for j in range(height):
			r = pixels[i, j][0]
			g = pixels[i, j][1]
			b = pixels[i, j][2]
			s = r+g+b
			if s>(( 255 + factor) // 2) * 3:
				r,g,b = 255,255,255
			else:
				r,g,b = 0,0,0
			pixels[i, j] = (r, g, b)

