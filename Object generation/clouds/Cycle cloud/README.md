[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
 ██████╗██╗      ██████╗ ██╗   ██╗██████╗      ██████╗██╗   ██╗ ██████╗██╗     ███████╗
██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗    ██╔════╝╚██╗ ██╔╝██╔════╝██║     ██╔════╝
██║     ██║     ██║   ██║██║   ██║██║  ██║    ██║      ╚████╔╝ ██║     ██║     █████╗  
██║     ██║     ██║   ██║██║   ██║██║  ██║    ██║       ╚██╔╝  ██║     ██║     ██╔══╝  
╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝    ╚██████╗   ██║   ╚██████╗███████╗███████╗
 ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝      ╚═════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝
                                                                                       
```
# Cloud Generation and Scene Setup

`Clouds` is a Python script for Blender that automates the generation of realistic clouds and sets up your scene with various lighting and environmental options. With adjustable parameters, this script allows for a customizable cloud generation experience.

[Capture vidéo du 04-11-2023 17:46:07.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/69b87b4f-ca8d-4d20-9b35-c94506f3fedc)

## Features:

1. **Metaball-based Cloud Generation**:
   - Generates clouds using Blender's metaball object, which are later converted to a mesh.
   - Parameters for controlling the number, size, and distance of metaballs.

2. **Volume Modifiers**:
   - Converts the mesh to a volume and applies a Volume Displace modifier with configurable strength.

3. **Texture Configuration**:
   - Creates a procedural cloud texture for the Volume Displace modifier.
   - Parameters for controlling texture type and size.

4. **Sky Shader Setup** (Optional):
   - Sets up a sky shader with an environment texture.
   - Optionally uses a Mix Shader for reflection, blending a color background with the environment texture based on the camera ray.
   - Parameters for controlling background color and reflection.

5. **Spotlight Creation** (Optional):
   - Adds a spotlight to illuminate the cloud.
   - Parameters for controlling the spotlight's distance and power.

6. **Material Assignment**:
   - Assigns a transparency material to the cloud mesh.

Btw you can find some sky image I've generated for this script on [art station here](https://www.artstation.com/artwork/qew98N)


![Capture d’écran du 2023-11-04 17-18-04](https://github.com/SECRET-GUEST/animation/assets/92639080/8cb2f485-8385-4ce8-8e11-723f1d9f227e)

## Usage:

1. **Setup**:
   - Ensure Blender is installed on your machine.
   - Download the `clouds.py` script from the repository.

2. **Running the Script**:
   - Open Blender.
   - Navigate to the `Scripting` tab.
   - Click `Open` to load the `clouds.py` script.
   - Adjust the parameters at the beginning of the script to suit your needs.
   - Press the `Run Script` button.

3. **Customization**:
   - Customize the cloud generation process by modifying the adjustable parameters at the beginning of the script.
   - Parameters include the number of metaballs, metaball size, distance between metaballs, voxel amount, displace strength, texture type, texture size, and more.
   - For sky shader and spotlight setup, toggle the `use_world_sky`, `use_world_reflexion`, and `spotlight_cloud` variables. Additionally, specify a link to an environment image for the sky shader using the `skylink` variable and set a background color using the `background_color_hex` variable.

## Parameters:

```python
# Adjustable Parameters
# Cloud:
num_metaballs = 15  # Number of metaballs
metaball_size = 3  # Base size of metaballs
distance = 3  # Distance between metaballs

# Volume:
voxel_amount = 108  # Voxel Amount parameter for Mesh to Volume modifier
strength = 2.0  # Strength parameter for Volume Displace modifier
texture_type = 'SOFT'  # Texture type: 'HARD' or 'SOFT'
cloud_texture_size = 2  # Texture size

# World Environment:
use_world_sky = True  # Only set an image for the world background
use_world_reflexion = True  # Set background + a reflective image
background_color_hex = "#0060D4"  # Default is blue
skylink = ""  # Link to the environment image for reflection

# Lights:
spotlight_cloud = True  # Create a spotlight
spotlight_distance = 20.0  # Distance of the spotlight
lumens = 20000  # Power of the spotlight
```

Experiment with different parameter values to achieve the desired cloud and scene setup.

![Capture d’écran du 2023-11-04 19-23-39](https://github.com/SECRET-GUEST/animation/assets/92639080/07a4bb6d-52eb-472d-8d8f-b433184684e6)
