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