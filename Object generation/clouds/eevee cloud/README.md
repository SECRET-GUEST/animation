[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███████╗███████╗██╗   ██╗███████╗███████╗     ██████╗██╗      ██████╗ ██╗   ██╗██████╗ 
██╔════╝██╔════╝██║   ██║██╔════╝██╔════╝    ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗
█████╗  █████╗  ██║   ██║█████╗  █████╗      ██║     ██║     ██║   ██║██║   ██║██║  ██║
██╔══╝  ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══╝      ██║     ██║     ██║   ██║██║   ██║██║  ██║
███████╗███████╗ ╚████╔╝ ███████╗███████╗    ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔
╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝     ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
```
# Procedural Cloud Generation Script for Blender

This script for Blender facilitates the procedural generation of clouds within a 3D scene. Clouds are created using a cube as a container, and a procedural **material** is applied to generate the cloud appearance. Additionally, the script also allows for the configuration of a sky environment with or without reflection, depending on whether an environment image is provided.

#### [Btw, here is a tutorial to explain how to make the same effect that I used to the script](https://www.youtube.com/watch?v=GhMQN4vVMIU&ab_channel=CGMatter)
[Capture vidéo du 05-11-2023 00:54:35.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/b2bee779-29cb-41f5-b23f-dd46d9f2e69e)

## Features

- Procedural cloud generation with a custom material.
- Sky environment configuration with or without reflection.
- Configurable options to adjust the appearance of clouds and sky.
- Neat organization of generated elements within a specific collection.

Example using eevee :
![evee](https://github.com/SECRET-GUEST/animation/assets/92639080/28b968ca-5426-4b14-a334-e220288c56a1)

## Usage
1. Copy the above script into a new text editor within Blender.
2. Adjust the parameters to your preferences:
   - `cloud_size_x` and `cloud_size_y` for the dimension of the container cube.
   - `color_ramp_position`, `noise_texture_scale`, and `noise_texture_detail` for cloud appearance.
   - `use_world_sky` to choose whether a sky environment should be created.
   - `background_color_hex` for the sky background color.
   - `skylink` for the path to an environment image for reflection (leave empty for none).
3. Run the script.

Example using cycles :
![cycles](https://github.com/SECRET-GUEST/animation/assets/92639080/9e210c76-7936-43e6-bb5a-beb4e6742be6)

## Results

- A cube named "cloud" will be created and placed in a collection called "clouds".
- A procedural material named "pro_cloud" will be created and applied to the cube.
- If `use_world_sky` is enabled, a sky environment will be set up with or without reflection depending on the `skylink` value.

## Customization

You can customize the appearance of clouds and sky by modifying the values of the parameters at the beginning of the script. You can also extend or modify the script to meet your specific needs for cloud generation and sky environment setup.

Nodes :
![Capture d’écran du 2023-11-05 01-05-56](https://github.com/SECRET-GUEST/animation/assets/92639080/aaae724c-2430-4139-945c-3b40363a25a0)
