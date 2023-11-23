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
This script for Blender 4.0 automates the process of importing various 3D file formats. It scans a specified directory and imports all recognizable 3D files based on their file extensions. Ideal for streamlining workflows involving multiple 3D files of different formats, this script also includes options for including subfolders, adding delays between imports, and organizing imported objects into collections to manage large batches of files efficiently.

While not faster than certain drag & drop solutions available online, it's free and effective.

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

Note: Some formats may require additional plugins or addons to be installed in Blender.

## Installation
1. Ensure you have Blender 4.0 or newer installed.
2. Download the `import_3d_files.py` script from this repository.
3. Open Blender, go to the scripting section, and drag & drop the script there.

## Configuration
- Modify the `folder_path` variable in the script to the path of your directory containing 3D files.
- Set `include_subfolders` to `True` if you want to include subfolders in the import process.
- Adjust `import_delay` to add a delay (in seconds) between each file import, which can be useful for managing large batches of files.
- Configure `include_in_a_single_collection` and `include_in_object_collection` to control how imported objects are organized into collections.

###### note : When both `include_in_a_single_collection` and `include_in_object_collection` are `True`, all objects are imported into a single "imported" collection, with each object also placed in its sub-collection named after the file.

The script will iterate through all files in the specified folder (and subfolders, if enabled) and attempt to import them into the current Blender project, organizing them into collections based on the configuration. Unsupported file formats or files that lead to import errors will be logged in the console.

## Recommendations
- Test the script with a small number of files first to ensure compatibility with your Blender setup.
- For large batches of files, gradually increase the `import_delay` to prevent Blender from becoming unresponsive.
- Regularly save your Blender project when using this script to import a large number of files.


