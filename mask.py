from PIL import Image, ImageFilter
from util import readImages
MASK_TRESHOLD = 50

background = Image.open("background.png")
images = readImages()

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


def mask(images):
    images_pixels = []
    mask = []
    for img in images_normalized:
        images_pixels.append(img.load())
        mask = diff(images_pixels[i]-background)

    return mask


def get_mask(image1, image2):
    _images = [image1,image2]#normalize((image1,image2))
    pixel1 = _images[0].load()
    pixel2 = _images[1].load()
    
    new_img = Image.new("RGB",(_images[0].size[0], _images[0].size[1]) )
    new_pixels = new_img.load()
    print( pixel1[707,542])
    print( pixel2[707,542])
    for x in range(_images[0].size[0]):
        for y in range(_images[0].size[1]):
            r1,g1,b1 = pixel1[x,y]
            r2,g2,b2 = pixel2[x,y]
            if abs(r1-r2) < MASK_TRESHOLD or abs(g1-g2) < MASK_TRESHOLD or abs(b1-b2) < MASK_TRESHOLD :
               new_pixels[x,y] = (255,255,255)
            else:
               
                new_pixels[x,y] = (0,0,0)
    return new_img


def add(image1, image2):
    
    images = normalize((image1,image2))
    pixel1 = images[0].load()
    pixel2 = images[1].load()
    
    new_img = Image.new("RGB",(images[0].size[0], images[0].size[1]) )
    new_pixels = new_img.load()
    
    for x in range(images[0].size[0]):
        for y in range(images[0].size[1]):
            r1,g1,b1 = pixel1[x,y]
            r2,g2,b2 = pixel2[x,y]
            new_pixels[x,y] =  (r1+r2,g1+g2,b1+b2)
       
      
    return new_img

def get_masks2(count):
    nrmImages = normalize(images)
    masks = []
    for im in nrmImages[0:count]:
        masks.append(diff(background,im))
    return masks


# masks = get_masks(1)
# result = background
# #for mask in masks:
#  #   result = add(mask,result) 

result = get_mask(background,images[0]) 
print(images[0].size)
print(background.size)
print(result.size)
result.show()


