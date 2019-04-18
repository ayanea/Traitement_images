import os
from PIL import Image, ImageFilter
def readImages():
    path = r"images\monsieur"
    images = []
    tmp = os.listdir(path)  # on met dans tmp tous les fichiers du chemin d'acces path
    for img_name in tmp:
        if img_name.lower().find('png') != -1 : 
            img =  Image.open(path + '/' + img_name )
            images.append(img) # pour chaque image de tmp, si on trouve l'extension png on l'ajoute a image

    #ou
    # for img_name in tmp:
    #     parts = img_name.split('.')
    #     if parts[1].lower() == 'png' : images.append(img)

    return images 

def readImages2(nb):
    path = r"images\monsieur"
    images = []
    tmp = os.listdir(path)  
    cpt = 0
    for img_name in tmp:
        if img_name.lower().find('png') != -1 and cpt%nb == 0  : 
            img =  Image.open(path + '/' + img_name )
            images.append(img)
        cpt += 1

    return images 