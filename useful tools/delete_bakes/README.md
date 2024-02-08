[![Blender](https://img.shields.io/badge/Blender-4.0-orange.svg)](https://www.blender.org/download/releases/4.0/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██████╗ ███████╗██╗     ███████╗████████╗███████╗    ██████╗  █████╗ ██╗  ██╗███████╗███████╗
██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝
██║  ██║█████╗  ██║     █████╗     ██║   █████╗      ██████╔╝███████║█████╔╝ █████╗  ███████╗
██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝      ██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ╚════██║
██████╔╝███████╗███████╗███████╗   ██║   ███████╗    ██████╔╝██║  ██║██║  ██╗███████╗███████║
╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
```
# Bake clear

This repository contains a script (`remove_bakes.py`) designed to remove baked images from a Blender project... I honestly don't know why I'm doing this.

## Usage

To use this script:

1. Open Blender and load your project.
2. Open the Scripting workspace.
3. Open the `remove_bakes.py` file in the text editor.
4. Run the script by clicking the "Run Script" button or pressing Alt + P.
5. The script will iterate over all images loaded in the project and remove any images with "Bake" in their name.
6. Once the script has finished, a message will be displayed confirming the removal of baked images.

## Script Explanation

This script iterates over all images loaded in Blender and removes any images with "Bake" in their name. Baked images are typically generated during baking processes (e.g., texture baking) and may no longer be needed after the baking process is complete. Removing these baked images can help keep your project clean and reduce file size.

