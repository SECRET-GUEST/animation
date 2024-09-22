![Batch Script](https://img.shields.io/badge/script-batch-DDFF00)
![STABLE](https://img.shields.io/badge/VERSION-1.0.0-green) 
![VINDWOS](https://img.shields.io/badge/vVINDWOS-blue)
```
███████╗███████╗███╗   ███╗██████╗ ███████╗ ██████╗     ██████╗ ██╗     ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔════╝████╗ ████║██╔══██╗██╔════╝██╔════╝     ██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  █████╗  ██╔████╔██║██████╔╝█████╗  ██║  ███╗    ██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝  ██║   ██║    ██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║     ██║ ╚═╝ ██║██║     ███████╗╚██████╔╝    ██████╔╝███████╗███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```
# Batch Scripts for FFMPEG Video Rendering

This repository contains two batch scripts designed to help automate the process of rendering image sequences into video files using FFMPEG. These scripts support both horizontal and vertical formats and are intended to convert rendered image sequences (e.g., from Blender) into high-quality video files.

## Purpose

These batch scripts are specifically designed to process PNG image sequences rendered from Blender. You can easily modify the scripts to work with other image formats, such as JPEG. By default, the scripts use the PNG format for high-quality, lossless video rendering.

## Requirements

1. **FFMPEG**: FFMPEG is a free, open-source tool used for converting, recording, and streaming multimedia. You will need to install FFMPEG and add it to your system’s PATH to run these scripts.

   - You can download FFMPEG from the official website: [FFMPEG Download Page](https://ffmpeg.org/download.html).
   - After downloading, follow these [instructions to add FFMPEG to your system’s PATH](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/). This step is crucial for the scripts to work correctly from any location on your system.

2. **Image Sequence**: Your images must be named sequentially in a format like `0001.png`, `0002.png`, etc., and placed in a folder named `pics` located in the same directory as the batch file. These images will be compiled into a video.

## How to Use the Scripts

### Horizontal Video Rendering

This script takes a sequence of images (in PNG format) and compiles them into a horizontal 4K video (3840x2160). 

- Place your image sequence in a folder named `pics` in the same location as the batch file.
- Run the batch file to generate a video file named `0000.mov` using FFMPEG.

### Vertical Video Rendering

This script works similarly but is designed for vertical 2160x3840 videos, often used in social media or mobile platforms.

- Place your vertical image sequence in the `pics` folder.
- Run the vertical batch script, which generates a video file named `0000_vertical.mov`.

## Understanding the FFMPEG Command

The core functionality of both scripts relies on the following FFMPEG command:

```bash
ffmpeg -r 30 -f image2 -s 3840x2160 -i %04d.png -vcodec libx264 -crf 0 -pix_fmt yuv420p 0000.mov
```

### Explanation:

- `-r 30`: Sets the frame rate to 30 frames per second.
- `-f image2`: Tells FFMPEG that the input will be an image sequence.
- `-s 3840x2160`: Specifies the resolution of the output video (in this case, 4K for horizontal format).
- `-i %04d.png`: This tells FFMPEG to use a sequence of PNG images named in a numeric order, such as `0001.png`, `0002.png`, etc. The `%04d` part indicates a four-digit numbering pattern.
- `-vcodec libx264`: Specifies the video codec to use, in this case, `libx264`, which is widely supported and offers efficient compression.
- `-crf 0`: Sets the quality of the output. A CRF (Constant Rate Factor) of 0 means lossless quality (the highest possible quality).
- `-pix_fmt yuv420p`: Specifies the pixel format, ensuring the video is widely compatible with media players.
- `0000.mov`: The name of the resulting video file, 0000 to make it top.

### Modifying the Command

- **For JPEG images**: If your image sequence is in JPEG format, simply change the `-i` part of the command to refer to JPEG files like this:
  
  ```bash
  -i %04d.jpg
  ```

- **Changing resolution**: You can adjust the resolution by changing the `-s` parameter. For example, to render a Full HD video, you could use:
  
  ```bash
  -s 1920x1080
  ```

## How to Use the Scripts with Shortcuts

You can place shortcuts to these batch files on your desktop or anywhere else on your system. The scripts will still work as intended, as they dynamically determine their own location and will search for the `pics` folder in the same directory where the batch file resides.

### Steps:

1. Right-click on the batch script file and select "Create Shortcut."
2. Move the shortcut to your desired location (e.g., your desktop).
3. Double-click the shortcut to run the script. It will automatically locate the `pics` folder relative to the batch file's location.
