from PIL import Image
import numpy as np


IMGFILE = 'test.png' 


def find_closest_pallete_color(pixel): # black and white
    return 255 if pixel[0]>=128 else 0


def main():
    
    with Image.open(IMGFILE) as im:
        w,h = im.size
        pixels = im.load()

    for y in range(1, h-1):
        for x in range(1, w-1):
            oldpixel = pixels[x, y]
            newpixel = find_closest_pallete_color(oldpixel)
            pixels[x, y] = (newpixel,)*3
            quant_error = oldpixel[0] - newpixel
            pixels[x + 1, y    ] = (pixels[x + 1, y    ][0] + int(quant_error * 7 / 16),)*3
            pixels[x - 1, y + 1] = (pixels[x - 1, y + 1][0] + int(quant_error * 3 / 16),)*3
            pixels[x    , y + 1] = (pixels[x    , y + 1][0] + int(quant_error * 5 / 16),)*3
            pixels[x + 1, y + 1] = (pixels[x + 1, y + 1][0] + int(quant_error * 1 / 16),)*3
    
    im.show() 

if __name__ == "__main__":
    main()
