# Batch Scripts for FFMPEG Video Rendering

This repository contains two batch scripts designed to help automate the process of rendering image sequences into video files using FFMPEG. The scripts work for both horizontal and vertical formats and are designed to locate and execute inside the `pics` folder, based on the location of the batch file itself. This allows you to use the scripts even through shortcuts placed on the desktop, without worrying about incorrect folder paths.

## Scripts

### 1. Horizontal Video Rendering (`horizontal_video_render.bat`)

This script renders a horizontal 3840x2160 video (4K) from an image sequence.

#### Usage

1. Ensure the folder containing the script also has a subfolder named `pics`, which contains the image sequence files.
2. Place the batch file in any directory and create a shortcut to it on your desktop (if desired).
3. Run the script to convert images from the `pics` folder into a video.
