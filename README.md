# Projet_Python


Telecharger la librairie ffmpeg à l’adresse suivante: https://www.google.com/url?q=https://ffmpeg.zeranoe.com/builds/&sa=D&source=hangouts&ust=1558784352806000&usg=AFQjCNE4MkEOIb4ALQATS1YtHT5l7WcY2g  version 20190524-1d74150

Modifier les variables d’environnement du path en ajoutant une nouvelle variable avec le chemin d’accès du dossier bin situé dans le dossier télécharger, par exemple :  C:\Users\DELL\Documents\E2\ffmpeg-20190524-1d74150-win64-static\bin

Dans le cmd faire pip install ffmpeg-python

Lancer photosequence.py avec la commande suivante (écrite dans le README ):  
      python nomFichier.py -i nomVideo.mp4 -fi 4
par exemple : python photosequence.py -i monsieur.mp4 -fi 4
              python photosequence.py -i jaguar.mp4 -fi 6


python photosequence.py -i monsieur.mp4 -fi 4
python photosequence.py --video <CHEMIN_VIDEO> --frame_interval <INTERVAL_FRAME>