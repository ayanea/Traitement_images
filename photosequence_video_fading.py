from PIL import Image, ImageFilter
from lib.util import readImages_and_masks,normalize, extract_frames_from_video, printProgressBar
from lib.background import get_background_and_save
from lib.mask import get_mask_and_save
import os
import argparse
import ffmpeg

def mix_alpha(v1,v2, alpha):
    return int((v1*alpha+v2*(100-alpha))/100)


def binary_merge(item,img_result,transparency):
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
                if transparency != -1:
                    r2,g2,b2 = img_result_pixels[x,y]
                    r = mix_alpha(r1,r2, transparency)
                    g = mix_alpha(g1,g2, transparency)
                    b = mix_alpha(b1,b2, transparency)
                    img_result_pixels[x,y] = (r,g,b)
                else:
                    img_result_pixels[x,y] = ( r1,g1,b1)

def photosequence_video(frame_interval,video_sequence_interval, background, tmp_folder, path_video):
    images = readImages_and_masks(frame_interval, tmp_folder)
   
    print("----------------------  DEBUT DE LA SAUVEGARDE DE LA VIDEO FINALE 4/4 ------------------------------------------")
    N = len(images)
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    cpt = 0
    ratio = 100/N
    basename = os.path.splitext(os.path.basename(path_video))[0]
    frozen_characters_img = background.copy()
    binary_merge(images[0], frozen_characters_img,-1)
    for i in range(0,N):
            print(cpt,'  ')
            img_result = frozen_characters_img.copy()
            binary_merge(images[i], img_result,ratio*i+1)
            fileName = ''.join(['img-fading-{:07d}'.format(cpt),'.png'])
            filePath = os.path.join(tmp_folder,fileName)
            img_result.save(filePath)
            if cpt%video_sequence_interval == 0:
                 binary_merge(images[i], frozen_characters_img,ratio*i+1)
            printProgressBar(cpt, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
            cpt += 1

    images_to_video(tmp_folder,'img-fading-%07d.png',''.join([basename,'-fading','.mp4']))   
    print("---------------------- VIDEO SAUVEGARDEE !  ------------------------------------------")
    print()

def images_to_video(directory,input_file_prefix, output_file_name):
   print('********* PATH',os.path.join(directory, input_file_prefix))
   stream = ffmpeg.input(os.path.join(directory, input_file_prefix),start_number=1, framerate =15)
   stream = ffmpeg.output(stream,  os.path.join(directory, output_file_name), vcodec='libx264',pix_fmt='yuv420p',crf=18)
   ffmpeg.run(stream)


if __name__ == "__main__":
   #usage example : python photosequence_video_fading.py -i monsieur.mp4 -fi 1 -vsi 15
                    #python photosequence_video_fading.py -i jaguar.mp4 -fi 1 -vsi 20
   if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--video", type=str, help="Chemin du fichier vidéo")
    parser.add_argument("-fi", "--frame_interval", type=int, default=4, help="Interval des frames à prendre pour le mask")
    parser.add_argument("-vsi", "--video_sequence_interval", type=int, default=15)
    args = parser.parse_args()

    FRAME_INTERVAL = args.frame_interval
    VIDEO_SEQUENCE_INTERVAL = args.video_sequence_interval
    if args.video is not None:
        tmp_folder = extract_frames_from_video(args.video,15)   #Extract frames from video with ffmpeg
        background = get_background_and_save(tmp_folder) #get background from frames and save
        get_mask_and_save(tmp_folder, background, FRAME_INTERVAL)   #get mask and save
        photosequence_video(FRAME_INTERVAL,VIDEO_SEQUENCE_INTERVAL, background, tmp_folder, args.video)   #save photosequence in main directory
        #photosequence_video(FRAME_INTERVAL, VIDEO_SEQUENCE_INTERVAL,background, tmp_folder, args.video)

        
    else:
        print("Aucun fichier vidéo n'a été donnée en entrée")
        exit(1)
    
    
    #images_to_video('C:/Users/DELL/Documents/E2/Traitement_images/tmp/Test','image-%07d.png','out.mp4')
   