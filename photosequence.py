from PIL import Image, ImageFilter
from util import readImages_and_masks,normalize


def binary_merge(bkg_img, item,img_result):
    _images = normalize([bkg_img,item[0],item[1],img_result])
    bkg_pixels = _images[0].load()
    img_pixels = _images[1].load()
    mask_img = _images[2].load()
    width = _images[0].size[0]
    height = _images[0].size[1]
    img_result_pixels = _images[3].load()
       
    for x in range(width):
        for y in range(height):
            r1,g1,b1 = bkg_pixels[x,y]
            r2,g2,b2 = img_pixels[x,y]
            
            if mask_img[x,y] == (0,0,0):
                img_result_pixels[x,y] = (r2,g2,b2)
       

background = Image.open("background.png")
images = readImages_and_masks(4)

img_result = background#Image.new("RGB",(background.size[0], background.size[1]) )
for item in images:
    binary_merge(background, item,img_result)

img_result.save("photosequence.png")