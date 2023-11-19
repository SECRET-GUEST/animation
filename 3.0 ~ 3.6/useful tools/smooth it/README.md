[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███████╗███╗   ███╗ ██████╗  ██████╗ ████████╗██╗  ██╗    ██╗████████╗
██╔════╝████╗ ████║██╔═══██╗██╔═══██╗╚══██╔══╝██║  ██║    ██║╚══██╔══╝
███████╗██╔████╔██║██║   ██║██║   ██║   ██║   ███████║    ██║   ██║   
╚════██║██║╚██╔╝██║██║   ██║██║   ██║   ██║   ██╔══██║    ██║   ██║   
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██║    ██║   ██║   
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝    ╚═╝   ╚═╝   
```
# Smooth script

This Blender script allows you to apply Auto Smooth and/or a Subdivision Surface modifier to all selected objects in your scene.

## Features

- Apply Auto Smooth with a customizable angle to all selected objects.
- Apply a Subdivision Surface modifier with customizable subdivision levels to all selected objects.
- Toggle the use of Auto Smooth and Subdivision Surface modifier independently.

## Installation

1. Open Blender.
2. Go to the Text Editor view.
3. Create a new text data-block.
4. Copy and paste the script into the text data-block.
5. Save the script to a file by clicking on the "Text" menu, then "Save As".

## Usage

1. Select the objects you want to smooth in your Blender scene.
2. Open the Text Editor view.
3. Open the script file you saved earlier.
4. Adjust the user parameters at the beginning of the script as needed:
   - `auto_smooth_angle`: The angle for Auto Smooth in degrees (default is 30.0).
   - `subdiv_levels`: The number of subdivision levels for the Subdivision Surface modifier (default is 2).
   - `use_auto_smooth`: Set to `True` to enable Auto Smooth, `False` to disable (default is `True`).
   - `use_subsurf_mod`: Set to `True` to enable the Subdivision Surface modifier, `False` to disable (default is `True`).
5. Click on the "Run Script" button to execute the script.
