# Projet_Python


Telecharger la librairie ffmpeg à l’adresse suivante: https://www.google.com/url?q=https://ffmpeg.zeranoe.com/builds/&sa=D&source=hangouts&ust=1558784352806000&usg=AFQjCNE4MkEOIb4ALQATS1YtHT5l7WcY2g  version 20190524-1d74150

Modifier les variables d’environnement du path en ajoutant une nouvelle variable avec le chemin d’accès du dossier bin situé dans le dossier télécharger, par exemple :  C:\Users\DELL\Documents\E2\ffmpeg-20190524-1d74150-win64-static\bin

Dans le cmd faire pip install ffmpeg-python

Lancer photosequence.py avec la commande suivante (écrite dans le README ):  
      python nomFichier.py -i nomVideo.mp4 -fi 4
par exemple : python photosequence.py -i monsieur.mp4 -fi 4
              python photosequence.py -i jaguar.mp4 -fi 6

              python photosequence_fading.py -i monsieur.mp4 -fi 4
              python photosequence_fading.py -i jaguar.mp4 -fi 6

              python photosequence_video.py -i monsieur.mp4 -fi 1 -vsi 15
              python photosequence_video.py -i jaguar.mp4 -fi 1 -vsi 20

              python photosequence_video_fading.py -i monsieur.mp4 -fi 1 -vsi 15
              python photosequence_video_fading.py -i jaguar.mp4 -fi 1 -vsi 20


python photosequence.py -i monsieur.mp4 -fi 4
python photosequence.py --video <CHEMIN_VIDEO> --frame_interval <INTERVAL_FRAME>

Les fichiers photosequence.py, photosequence_fading.py, photosequence_video.py et photosequence_video_fading.py se trouvent dans le dossier courant.
Les fichiers background.py, util.py et mask.py se trouvent dans le dossier lib
Les images des sujets, de leurs masks et les résulats des videos de la photosequence (avec ou sans fading) se trouvent dans le dossier tmp. Il faut d'abord lancer les programmes pour les voir.
Les images de la photosequence (avec ou sans fading) se trouvent dans le dossier courant