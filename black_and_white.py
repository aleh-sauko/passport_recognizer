BLACK_COLOR = 0
WHITE_COLOR = 255

def process(image, factor):
    width, height = image.size
    pixels = image.load()
    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]
            r, g, b = pixel[0], pixel[1], pixel[2]

            sum = r + g + b

            if sum > (((WHITE_COLOR + factor) // 2) * 3):
                r, g, b = WHITE_COLOR, WHITE_COLOR, WHITE_COLOR
            else:
                r, g, b = BLACK_COLOR, BLACK_COLOR, BLACK_COLOR

            pixels[col, row] = (r, g, b)

    image.show()
