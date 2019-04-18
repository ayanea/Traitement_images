from PIL import Image, ImageFilter
from util import readImages

def normalize(images):
    minW = images[0].size[0]
    minH = images[0].size[1]
    maxW = images[0].size[0]
    maxH = images[0].size[1] #on initialise les variables min et max aux dimensions 
    #de la premiere image pour la comparer avec les suivantes   
    for i in images:
        nvimages = []
        hauteur = []
        largeur = []
        hauteur.append(i.size[1])
        largeur.append(i.size[0]) #pas obligatoire de faire un tableau pour hauteur et largeur (inutile?!)

        if(hauteur[0] <= minH ):
            minH = hauteur[0]
        elif (hauteur[0] >= maxH):
            maxH = hauteur[0]
                
        if (largeur[0] <= minW):
            minW = largeur[0]
        elif (largeur[0] >= maxW) :
            maxW = largeur[0]
            
    if (minW == maxW and minH == maxH):
        return images
    
    for i in images:
        nvimages.append(crop(i, 0, 0, minH, minW))
    
    return nvimages

def binary_merge(bkg_img, img,mask, img_result):
    _images = normalize([bkg_img,img,mask,img_result])
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
               mask_img [x,y] = (r1,g1,b1)
                
            #else:
                #img_result_pixels[x,y] = (r1,g1,b1)
       

background = Image.open("background.png")
mask = Image.open("mask.png")
images = readImages(4)

img_result = background#Image.new("RGB",(background.size[0], background.size[1]) )
for img in images[0:10]:
    binary_merge(background, img, mask,img_result)
    mask.show()

img_result.show()