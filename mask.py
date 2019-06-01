from PIL import Image, ImageFilter
from util import readImages,normalize
MASK_TRESHOLD = 50 


def create_image(color):
    img = Image.new("RGB",(background.size[0], background.size[1]) )
    pixels = img.load()
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            pixels[x,y] = color
    return img
   

def get_mask_old(bkg_img, img,img_result): #permet de creer une seule image avec tous les masques
   
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
   

def get_mask(bkg_img, img): #permet de creer un masque pour chaque image 
   
    mask_image = create_image((255,255,255)) # on creer une image blanche 
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
            # on compare chaque difference de pixels a une constante qui represente un taux d'erreur
            is_background = abs(r1-r2) < MASK_TRESHOLD and abs(g1-g2) < MASK_TRESHOLD and abs(b1-b2) < MASK_TRESHOLD 
            if not is_background:
              img_mask_pixels[x,y] = (0,0,0) # on met les pixels de l'image en noir

    return mask_image


background = Image.open("background.png")
images = readImages(4) # selectionne toutes les 4 images

for im in images:
    mask = get_mask(background, im)
    fileparts  = im.filename.split('.')
    maskFileName = fileparts[0] + '_mask.' + fileparts[1]
    mask.save(maskFileName)

 