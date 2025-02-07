[![Blender](https://img.shields.io/badge/Blender-4.3.2-orange.svg)](https://www.blender.org/download/releases/4-3/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██╗    ██╗ █████╗ ███████╗██╗  ██╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║    ██║██╔══██╗██╔════╝██║  ██║    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║ █╗ ██║███████║███████╗███████║    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║███╗██║██╔══██║╚════██║██╔══██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
╚███╔███╔╝██║  ██║███████║██║  ██║    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
```

#  Project Cleanup 

This Blender script provides a comprehensive cleanup of a Blender project. It's designed to clear simulation caches, delete all keyframes, and remove unused materials, textures, meshes, images, collections, UV maps, and node groups.

![cleaner](https://user-images.githubusercontent.com/92639080/229263110-c3ee2099-e29b-465e-a7cd-9779145d0a69.gif)


## Features

- **Clear Simulation Caches**: Clears caches for particle systems, fluids, smoke, gas, cloth, soft bodies, and rigid bodies.
- **Delete All Keyframes**: Removes all animation keyframes from objects, materials, cameras, lights, and curves.
- **Remove Unused Data Blocks**: Deletes unused materials, textures, meshes, images, and collections.
- **Clear Orphaned Data**: Removes data blocks that are no longer used in the project.
- **Delete Unused UV Maps**: Clears UV Maps that are not used by any materials.
- **Remove Unused Node Groups**: Deletes node groups that are not used in any material nodes.

## Configuration

At the top of the script, several variables can be set to 'y' (yes) or any other value for 'no' to control what the script clears:

- `clear_caches`: Clear simulation caches
- `clear_keyframes`: Delete all keyframes
- `clear_unused_materials`: Remove unused materials
- `clear_unused_textures`: Remove unused textures
- `clear_unused_meshes`: Remove unused meshes
- `clear_unused_images`: Remove unused images
- `clear_unused_collections`: Remove unused collections
- `clear_orphan_data`: Clear orphaned data
- `clear_unused_uv_maps`: Delete unused UV maps
- `clear_unused_node_groups`: Remove unused node groups

## Usage

1. Open your Blender project.
2. Run the script in Blender's Text Editor.
3. Based on your configuration, the script will clean up the project.

## Caution

This script will irreversibly modify your Blender project. It's recommended to save a backup of your project before running the script.


