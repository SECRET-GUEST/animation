[![Blender](https://img.shields.io/badge/Blender-4.1-orange.svg)](https://www.blender.org/download/releases/4-1/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██████╗  █████╗ ████████╗ ██████╗██╗  ██╗    ███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║   ██║   ██║     ███████║    █████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
██╔══██╗██╔══██║   ██║   ██║     ██╔══██║    ██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║   ██║   ╚██████╗██║  ██║    ███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                               
```
# Blender GLB Batch Exporter

## Overview
The Blender GLB Batch Exporter is a Python script for Blender, designed to streamline the process of exporting multiple armatures and their associated objects to the GLB format. This script is particularly useful for projects involving numerous animated characters or objects, simplifying the export process and ensuring consistency across exported files.

## Features
- Automatically exports armatures and their child objects to GLB format.
- Sequentially names and saves the exported files for easy identification and organization.
- Customizes export settings optimized for Three.js, including the export of animations and setting the Y-axis as the vertical axis.

## Prerequisites
To use this script, ensure you have Blender installed on your machine. This script is specifically designed for Blender and may not be compatible with other 3D modeling software.

## Installation
1. Download the `blender_glb_batch_exporter.py` file.
2. Open the Blender project from which you wish to export objects.
3. In Blender, open the Text Editor view.
4. Click 'Open' and select the downloaded script.

## Usage
1. Modify the `output_folder` variable in the script to specify the directory where you want the exported GLB files to be saved.
2. Run the script in Blender by navigating to the Text Editor view where you opened the script and pressing the 'Run Script' button.

The script will automatically identify all armatures in your Blender project, select each armature and its child objects, and export them to the specified directory in the GLB format.

## Output
The output of the script will be a series of GLB files, each containing an armature and its associated objects. The files are saved in the specified directory and are named sequentially (e.g., dancer1.glb, dancer2.glb, etc.).