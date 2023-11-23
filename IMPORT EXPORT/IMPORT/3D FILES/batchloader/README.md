[![Blender](https://img.shields.io/badge/Blender-4.0-orange.svg)](https://www.blender.org/download/releases/4.0/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██████╗  █████╗ ████████╗ ██████╗██╗  ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║   ██║   ██║     ███████║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██╔══██╗██╔══██║   ██║   ██║     ██╔══██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

# Blender 3D File Importer Script

## Overview
This script for Blender 4.0 automates the process of importing various 3D file formats. It scans a specified directory and imports all 3D files it can recognize, based on their file extensions. This tool is ideal for streamlining workflows that involve working with multiple 3D files of different formats.

## Supported File Formats
The script supports a wide range of 3D file formats, including but not limited to:
- OBJ (`.obj`)
- FBX (`.fbx`)
- STL (`.stl`)
- COLLADA (`.dae`)
- PLY (`.ply`)
- 3DS (`.3ds`)
- GLTF/GLB (`.gltf`, `.glb`)
- X3D (`.x3d`)
- Alembic (`.abc`)
- BVH (`.bvh`)
- SVG (for curves, `.svg`)
- LightWave (`.lwo`)
- VRML97 (`.vrml`, `.wrl`)
- DXF (`.dxf`)

Please note that some formats may require additional plugins or addons to be installed in Blender.

## Installation
1. Ensure you have Blender 4.0 or newer installed.
2. Download the `import_3d_files.py` script from this repository.
3. Open Blender and go to put script in scripting section by drag&drop

## Modify the `folder_path` variable in the script to the path of your directory containing 3D files.

The script will iterate through all files in the specified folder and attempt to import them into the current Blender project. Unsupported file formats or files that lead to import errors will be logged in the console.

