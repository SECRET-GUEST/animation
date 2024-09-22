@echo off
REM Get the path of the batch script
set scriptDir=%~dp0

REM Change directory to the 'pics' folder inside the script's directory
cd /d "%scriptDir%\pics"

REM Run FFMPEG to render the video
ffmpeg -r 30 -f image2 -s 2160X3840 -i %%04d.png -vcodec libx264 -crf 0 -pix_fmt yuv420p 0000.mov
