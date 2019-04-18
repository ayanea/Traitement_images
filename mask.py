from PIL import Image, ImageFilter
from util import readImages
MASK_TRESHOLD = 50

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

def create_image(color):
    img = Image.new("RGB",(background.size[0], background.size[1]) )
    pixels = img.load()
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            pixels[x,y] = color
    return img
   

def get_mask_old(bkg_img, img,img_result):
   
    _images = normalize([bkg_img, img,img_result])
    bkg_pixels  = _images[0].load()
    img_pixels  = _images[1].load()
    img_result_pixels = _images[2].load()
    width = _images[0].size[0]
    height = _images[0].size[1]
    
    for x in range(width):
        for y in range(height):
            r1,g1,b1 = bkg_pixels[x,y]
            r2,g2,b2 = img_pixels[x,y]
            is_background = abs(r1-r2) < MASK_TRESHOLD and abs(g1-g2) < MASK_TRESHOLD and abs(b1-b2) < MASK_TRESHOLD 
            if not is_background:
              img_result_pixels[x,y] = (0,0,0)
   

def get_mask(bkg_img, img):
   
    mask_image  =  create_image((255,255,255))
    _images = normalize([bkg_img, img,mask_image])
    bkg_pixels  = _images[0].load()
    img_pixels  = _images[1].load()
    img_mask_pixels = _images[2].load()
    width = _images[0].size[0]
    height = _images[0].size[1]
    
    for x in range(width):
        for y in range(height):
            r1,g1,b1 = bkg_pixels[x,y]
            r2,g2,b2 = img_pixels[x,y]
            is_background = abs(r1-r2) < MASK_TRESHOLD and abs(g1-g2) < MASK_TRESHOLD and abs(b1-b2) < MASK_TRESHOLD 
            if not is_background:
              img_mask_pixels[x,y] = (0,0,0)

    return mask_image



background = Image.open("background.png")
images = readImages(4)

for im in images:
    mask = get_mask(background, im)
    fileparts  = im.filename.split('.')
    maskFileName = fileparts[0] + '_mask.' + fileparts[1]
    print(maskFileName)
    mask.save(maskFileName)


# result = get_mask(background,images[0]) 
# result.show()


 