import os
from PIL import Image, ImageFilter
def readImages():
    path = r"images\monsieur"
    images = []
    tmp = os.listdir(path)  # on met dans images2 tous les fichiers du chemin d'acces path
    for img_name in tmp:
        if img_name.lower().find('png') != -1 : 
            img =  Image.open(path + '/' + img_name )
            images.append(img) # pour chaque image de images2, si on trouve l'extension png on l'ajoute a image

    return images 
# ou