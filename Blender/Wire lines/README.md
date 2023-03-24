Blender 3.4 | Python
```
████████╗██╗  ██╗███████╗    ██╗    ██╗██╗██████╗ ███████╗
╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██║██╔══██╗██╔════╝
   ██║   ███████║█████╗      ██║ █╗ ██║██║██████╔╝█████╗  
   ██║   ██╔══██║██╔══╝      ██║███a██║██║██╔══██╗██╔══╝  
   ██║   ██║  ██║███████╗    ╚███╔███╔╝██║██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝
                                                          
```
![0](https://user-images.githubusercontent.com/92639080/227445971-8b68a52d-3321-4d1f-acb0-60003cbdb1cf.gif)

# Description

This script adds wireframe modifiers and materials to all mesh objects in a Blender scene. The wireframe material can be customized by changing the wire line or background scene color, and also the glow intensity, the thickness of the wireframe in settings at the top of the script. The wireframe is created using nodes in the material editor, allowing for flexibility in adjusting its appearance. The script also creates a new view layer specifically for the wireframe, making it easy to switch between viewing the wireframe and the normal render. 

![dsfs](https://user-images.githubusercontent.com/92639080/227446618-95926cdd-c7ef-4ef9-ad67-1c7107ea4525.png)


# Features:
- Customizable wireframe color, glow intensity, background color of the scene and thickness of the wireframe
- Uses nodes in the material editor to create the wireframe
- Automatically applies wireframe modifiers and materials to all mesh objects in the scene
- Creates a new view layer specifically for the wireframe

![0](https://user-images.githubusercontent.com/92639080/227445843-8e3ecf4a-091a-4539-919e-42611a630a10.gif)

# Usage:
1. Open Blender and open the Python console in the "scripting" last tab
2. Create new script, paste the wirelines.py in then run it by clicking on the "play" button.
3. You can easily ctrl+Z to make changes or go in the settings
4. The wireframe will be applied to all mesh objects in the scene and a new view layer for the wireframe will be created
5. To switch between viewing the wireframe and the normal render, select the appropriate view layer in the top-right corner of the Blender window

![0](https://user-images.githubusercontent.com/92639080/227446149-fc20cd0c-3908-42fb-b24b-85387750eb05.gif)
