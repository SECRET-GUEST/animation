[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███████╗███████╗██╗   ██╗███████╗███████╗     ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗
██╔════╝██╔════╝██║   ██║██╔════╝██╔════╝    ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝
█████╗  █████╗  ██║   ██║█████╗  █████╗      ██║     ██║     ██║   ██║██║   ██║██║  ██║███████╗
██╔══╝  ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══╝      ██║     ██║     ██║   ██║██║   ██║██║  ██║╚════██║
███████╗███████╗ ╚████╔╝ ███████╗███████╗    ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝███████║
╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝     ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
```
# Procedural Cloud Generation Script for Blender

This script for Blender facilitates the procedural generation of clouds within a 3D scene. Clouds are created using a cube as a container, and a procedural material is applied to generate the cloud appearance. Additionally, the script also allows for the configuration of a sky environment with or without reflection, depending on whether an environment image is provided.

## Features

- Procedural cloud generation with a custom material.
- Sky environment configuration with or without reflection.
- Configurable options to adjust the appearance of clouds and sky.
- Neat organization of generated elements within a specific collection.

## Usage

1. Copy the above script into a new text editor within Blender.
2. Adjust the parameters to your preferences:
   - `cloud_size_x` and `cloud_size_y` for the dimension of the container cube.
   - `color_ramp_position`, `noise_texture_scale`, and `noise_texture_detail` for cloud appearance.
   - `use_world_sky` to choose whether a sky environment should be created.
   - `background_color_hex` for the sky background color.
   - `skylink` for the path to an environment image for reflection (leave empty for none).
3. Run the script.

## Results

- A cube named "cloud" will be created and placed in a collection called "clouds".
- A procedural material named "pro_cloud" will be created and applied to the cube.
- If `use_world_sky` is enabled, a sky environment will be set up with or without reflection depending on the `skylink` value.

## Customization

You can customize the appearance of clouds and sky by modifying the values of the parameters at the beginning of the script. You can also extend or modify the script to meet your specific needs for cloud generation and sky environment setup.