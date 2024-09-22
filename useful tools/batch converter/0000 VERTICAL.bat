@echo off
REM Obtenir le chemin du dossier où se trouve le fichier batch
set scriptDir=%~dp0

REM Naviguer dans le dossier "pics" situé dans le même dossier que le batch
cd /d "%scriptDir%\pics"

REM Exécuter ffmpeg dans ce dossier
ffmpeg -r 30 -f image2 -s 2160X3840 -i %%04d.png -vcodec libx264 -crf 0 -pix_fmt yuv420p 0000.mov
