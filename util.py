import os
from PIL import Image, ImageFilter




def readImages(nb):
    path = r"images\monsieur"
    images = []
    tmp = os.listdir(path)  
    cpt = 0
    for img_name in tmp:
        if img_name.lower().find('_mask') != -1: continue
        if img_name.lower().find('png') != -1 and cpt%nb == 0  : 
            img =  Image.open(path + '/' + img_name )
            images.append(img)
        cpt += 1

    return images 

def readImages_and_masks(nb):
    path = r"images\monsieur"
    images = []
    tmp = os.listdir(path)  
    cpt = 0
    for img_name in tmp:
        if img_name.lower().find('_mask') != -1: continue
        if img_name.lower().find('png') != -1 and cpt%nb == 0  : 
            img =  Image.open(path + '/' + img_name )
            fileParts = img_name.split('.')
            mask_file_name = path + '/' + fileParts[0] + '_mask' + '.' +  fileParts[1] 
            img_mask =  Image.open(mask_file_name )
            images.append((img,img_mask))
        cpt += 1

    return images 


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
