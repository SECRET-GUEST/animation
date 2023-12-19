[![Blender](https://img.shields.io/badge/Blender-4.0-orange.svg)](https://www.blender.org/download/releases/4-0/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██████╗  █████╗ ██╗  ██╗███████╗    ███████╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║ ██╔╝██╔════╝    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║█████╔╝ █████╗      █████╗  ███████║███████╗   ██║   █████╗  ██████╔╝
██╔══██╗██╔══██║██╔═██╗ ██╔══╝      ██╔══╝  ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██╗███████╗    ██║     ██║  ██║███████║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```
# baking texture faster

This script is designed for Blender and allows users to bake the color of a material onto an object, preserving the appearance of the material even after applying a curve modifier. This is particularly useful for maintaining the appearance of striped or patterned materials on deformed objects.

[fdghdfg.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/e5eb77aa-33f0-44b4-b092-250dd7ed28e0)


## Features

- Bakes the color of a material onto a mesh object.
- Preserves the material appearance post curve modifier application.
- Customizable settings for texture resolution, file saving, and more.
- Creates a new material with the baked texture and applies it to the object.
- Option to save the baked texture as an image file.

## Requirements

- Blender (The script is tested with Blender 2.93, but should work with other versions).
- A mesh object with a material applied to it.

## Usage

1. **Setting Parameters**: 
   - Adjust the parameters at the beginning of the script according to your needs.
   - Parameters include texture width, height, image name, and the option to save the image.

2. **Running the Script**: 
   - Open your Blender project and select the mesh object you want to bake.
   - Open the Text Editor in Blender and paste the script.
   - Run the script by pressing the 'Run Script' button.

3. **Post-Bake**:
   - After running the script, the selected object will have a new material with the baked texture.
   - If `save_image` is set to `True`, the texture will be saved to the specified path.

## Customization

You can customize the script by modifying the following parameters:

- `texture_width` and `texture_height`: Resolution of the baked texture.
- `baked_img_name`: Name of the baked image.
- `new_material_name`: Name of the new material created.
- `save_image`: Set to `True` to save the image, or `False` to not save.
- `image_save_path`: Filepath to save the baked image.
