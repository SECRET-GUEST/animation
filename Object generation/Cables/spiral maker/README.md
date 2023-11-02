![Blender](https://img.shields.io/badge/Blender-orange)
![Python 3.10.13](https://img.shields.io/badge/Python-3.10.13-blue)
```
███████╗██████╗ ██╗██████╗  █████╗ ██╗         ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██║         ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
███████╗██████╔╝██║██████╔╝███████║██║         ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
╚════██║██╔═══╝ ██║██╔══██╗██╔══██║██║         ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
███████║██║     ██║██║  ██║██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

# Blender Spiral Generator Script

This script generates intertwined spirals in Blender which can be optionally converted into pipe structures.

## Features

- Generation of intertwined spirals with customizable parameters.
- Ability to extend the spirals outwards and/or inwards from both ends.
- Optional conversion of spirals into pipes with adjustable thickness using Blender's skin and subdivision surface modifiers.
- All spirals are organized in a Blender collection for easy manipulation.

## Usage

1. Ensure you have Blender installed on your machine.
2. Open Blender and create a new text data-block.
3. Copy the entire script and paste it into the text data-block.
4. Adjust the parameters at the beginning of the script to fit your requirements:
    - `number_of_spirals`: Sets the number of spirals to generate.
    - `height`: Sets the height of the spirals.
    - `revolutions`: Sets the number of revolutions the spirals make.
    - `radius`: Sets the initial radius of the spirals.
    - `create_pipes`: Set to `True` to convert spirals into pipes, `False` to keep them as curves.
    - `extend_outward`: Set to `True` to extend the last segments of the spirals outwards.
    - `extend_inward`: Set to `True` to extend the first segments of the spirals inwards.
    - `extension_length`: Sets the length of the extension.
    - `skin_thickness`: Sets the thickness of the pipes (if `create_pipes` is `True`).
    - `subdiv_levels`: Sets the subdivision level for smoothing the pipes (if `create_pipes` is `True`).

5. After adjusting the parameters, run the script by pressing the "Run Script" button.

The spirals will be generated in the scene, and if `create_pipes` is set to `True`, they will be converted into pipe structures.

