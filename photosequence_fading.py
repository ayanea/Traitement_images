from PIL import Image, ImageFilter
from lib.util import readImages_and_masks,normalize, extract_frames_from_video, printProgressBar
from lib.background import get_background_and_save
from lib.mask import get_mask_and_save
import os
import argparse

def fading(img,transparency):
    
    alpha =  (255*transparency)//100
    img_source =  img.copy()
    pixels_source = img_source.load()
    img_dest = Image.new("RGBA", img_source.size)
    pixels_destination = img_dest.load()
    width = img_source.size[0]
    height = img_source.size[1]

    for x in range (width):
        for y in range (height):
            r1,g1,b1 = pixels_source[x,y]
            pixels_destination[x,y] = r1,g1,b1,alpha


    return img_dest

def mix_alpha(v1,v2, alpha):
    return int((v1*alpha+v2*(100-alpha))/100)


def binary_merge(item,img_result,transparency):
    #img = fading(item[0],transparency)
    _images = normalize([item[0],item[1],img_result])
    img_pixels = _images[0].load()
    mask_img = _images[1].load()
    width = _images[0].size[0]
    height = _images[0].size[1]
    img_result_pixels = _images[2].load()
    
    for x in range(width):
        for y in range(height):
            if mask_img[x,y] == (0,0,0):        
                r1,g1,b1 = img_pixels[x,y]
                r2,g2,b2 = img_result_pixels[x,y]
                r = mix_alpha(r1,r2, transparency)
                g = mix_alpha(g1,g2, transparency)
                b = mix_alpha(b1,b2, transparency)
                img_result_pixels[x,y] = (r,g,b)
       
def photosequence(frame_interval, background, tmp_folder, path_video):
    images = readImages_and_masks(frame_interval, tmp_folder)
    img_result = background.convert('RGB')
    
    print("----------------------  DEBUT DE LA SAUVEGARDE DE L'IMAGE FINALE 4/4 ------------------------------------------")
    N = len(images)
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    cpt = 0
    ratio = 100//N
    for i in range(0,N):
        binary_merge(images[i], img_result,ratio*i + 1)
        cpt += 1
        printProgressBar(cpt, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    img_result.save("photosequence_fading_" + os.path.splitext(os.path.basename(path_video))[0] + ".png")
    print("---------------------- IMAGE SAUVEGARDEE !  ------------------------------------------")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--video", type=str, help="Chemin du fichier vidéo")
    parser.add_argument("-fi", "--frame_interval", type=int, default=4, help="Interval des frames à prendre pour le mask")
    args = parser.parse_args()

    FRAME_INTERVAL = args.frame_interval
    if args.video is not None:
        tmp_folder = extract_frames_from_video(args.video)   #Extract frames from video with ffmpeg
        background = get_background_and_save(tmp_folder) #get background from frames and save
        get_mask_and_save(tmp_folder, background, FRAME_INTERVAL)   #get mask and save
        photosequence(FRAME_INTERVAL, background, tmp_folder, args.video)   #save photosequence in main directory
    else:
        print("Aucun fichier vidéo n'a été donnée en entrée")
        exit(1)