[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███████╗██╗  ██╗████████╗██████╗ ██╗   ██╗██████╗ ███████╗     █████╗ ██╗     ██╗     
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██║     ██║     
█████╗   ╚███╔╝    ██║   ██████╔╝██║   ██║██║  ██║█████╗      ███████║██║     ██║     
██╔══╝   ██╔██╗    ██║   ██╔══██╗██║   ██║██║  ██║██╔══╝      ██╔══██║██║     ██║     
███████╗██╔╝ ██╗   ██║   ██║  ██║╚██████╔╝██████╔╝███████╗    ██║  ██║███████╗███████╗
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝
```

# Extrude all selected item in the right axe

This script for Blender automates the process of extruding selected mesh objects along specified axes (X, Y, and Z). It provides an easy way to apply uniform extrusion to multiple objects in a scene.

NOTE: After running the script, click on an empty space in Blender to refresh the interface.

[Capture vidéo du 11-11-2023 23:15:58.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/8a71a424-4c05-4574-8075-038db7be520a)


## Features

- **Selective Axis Extrusion**: Allows extrusion along any combination of the X, Y, and Z axes.
- **Customizable Extrusion Distance**: Set different extrusion distances for each axis.
- **Batch Processing**: Extrudes all selected mesh objects in the scene.

## Installation

1. **Blender Setup**:
   Ensure Blender is installed on your system. This script is compatible with Blender 2.8 and later versions.

2. **Script Download**:
   Download the `multi_axis_extrusion.py` script from this repository.

## Usage

1. **Open Blender**:
   Start Blender and open the project where you want to apply the extrusion.

2. **Select Objects**:
   In the 3D Viewport, select the mesh objects you wish to extrude.

3. **Run the Script**:
   - Open the Text Editor view in Blender.
   - Load the `multi_axis_extrusion.py` script.
   - Adjust the extrusion values (`extrude_x`, `extrude_y`, `extrude_z`) at the beginning of the script as needed.
   - Press `Run Script` to execute.

## Configuration

- Set `extrude_x`, `extrude_y`, and `extrude_z` to define the extrusion distance for each axis.
- Set any axis value to `0` or `None` to disable extrusion along that axis.

## Example

To extrude all selected objects by 0.5 units on the X-axis, 0 units on the Y-axis, and 0.3 units on the Z-axis, set the parameters as follows:

```python
extrude_x = 0.5
extrude_y = 0.0
extrude_z = 0.3
```
