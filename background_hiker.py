from PIL import Image, ImageFilter
import time
from util import readImages,normalize

def median_images(images):
    images_normalized = normalize(images)
    img_dest = Image.new("RGB", images[0].size)
    dest = img_dest.load()
    N = len(images)
    images_pixels = []
    for img in images_normalized:
        images_pixels.append(img.load())

    for y in range (images_normalized[0].size[1]):
        for x in range (images_normalized[0].size[0]):
            rp = []                     #listes pour les valeurs des pixels
            gp = []
            bp = []
            for i in range(N):          #pour travailler sur chaque pixel de chaque img
                pix = images_pixels[i]
                r1,g1,b1 = pix[x,y]
                rp.append(r1)           #valeurs rouge de chaque img
                gp.append(g1)           #valeurs verte de chaque img
                bp.append(b1)           #valeurs bleu de chaque img
            
            rp.sort()                   #trie des listes
            gp.sort()
            bp.sort()
            dest[x,y] = rp[N//2],gp[N//2],bp[N//2]     #la valeur med de chaque couleur
            
    return img_dest	

   
#start_time = time.time()
images =  readImages(1)
background = median_images(images)
background.save("background.png")
#duree = time.time() - start_time
#print("Duree: ",duree)