from PIL import Image, ImageFilter
import time
from lib.util import readImages,normalize, printProgressBar
import os

def fading(img,transparency):
    
    alpha =  (255*transparency)//100
    img_source =  img.copy()
    pixels_source = img_source.load()
    img_dest = Image.new("RGBA", img_source.size)
    pixels_destination = img_dest.load()
    width = img_source.size[0]
    height = img_source.size[1]

    for x in range (width):
        for y in range (height):
            r1,g1,b1 = pixels_source[x,y]
            pixels_destination[x,y] = r1,g1,b1,alpha


    return img_dest




img = Image.open('jaguar.png')
image = fading(img,50)
image.save("jaguar_fading.png", "PNG")



    
    
 