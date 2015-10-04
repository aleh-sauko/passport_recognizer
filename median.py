import numpy as np 
from PIL import Image, ImageDraw


def process(image, k):
	draw = ImageDraw.Draw(image)
	height = image.size[0]
	width = image.size[1]
	pix = image.load()
	for i in range(height):
		for j in range(width):
			vals = []
			for y in range(i-k/2,i+k/2+1):
				for x in range(j-k/2,j+k/2+1):
					r, c = y, x
					if (y < 0): r = 0
					if (x < 0): c = 0
					if (y >= height): r = height - 1 		
					if (x >= width): c = width - 1 	
					vals.append(pix[r,c][0]*(256**2)+pix[r,c][1]*256+pix[r,c][2])
			vals = np.sort(vals)	
			val = vals[len(vals)/2]
			r = val / (256**2)
			val -= r * (256**2)
			g = val / 256
			b = val % 256
			draw.point((i, j), (r, g, b)) 

if __name__ == "__main__":
	import sys
	image = Image.open(sys.argv[1])
	process(image, 3)
	image.save("res.jpg", "JPEG")
