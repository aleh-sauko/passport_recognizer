import math
import numpy as np
import convolve as convolve

def build_gauss_kernel(pixels, sigma, radius):
    size = radius * 2 + 1
    coeff  = 1 / (2 * math.pi * sigma * sigma)
    down   = 2 * sigma * sigma
    kernel = np.zeros((size, size))

    for row in range(-radius, radius + 1 ):
        for col in range(-radius, radius + 1):
            up = math.pow(row, 2) + math.pow(col, 2)
            kernel[row + radius, col + radius] = coeff * math.exp(- up / down)
    return kernel


def process(image, sigma, radius):
    width, height = image.size
    pixels = image.load()
    gauss_kernel = build_gauss_kernel(pixels, sigma, radius)

    convolve.process(image, gauss_kernel)
    # kernel_summ = np.sum(gauss_kernel)


    image.show()
