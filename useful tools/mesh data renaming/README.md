[![Blender](https://img.shields.io/badge/Blender-4.0-orange.svg)](https://www.blender.org/download/releases/4-0/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███    ███ ███████ ███████ ██   ██     ██████   █████  ████████  █████      ██████  ███████ ███    ██  █████  ███    ███ ███████ ██████  
████  ████ ██      ██      ██   ██     ██   ██ ██   ██    ██    ██   ██     ██   ██ ██      ████   ██ ██   ██ ████  ████ ██      ██   ██ 
██ ████ ██ █████   ███████ ███████     ██   ██ ███████    ██    ███████     ██████  █████   ██ ██  ██ ███████ ██ ████ ██ █████   ██████  
██  ██  ██ ██           ██ ██   ██     ██   ██ ██   ██    ██    ██   ██     ██   ██ ██      ██  ██ ██ ██   ██ ██  ██  ██ ██      ██   ██ 
██      ██ ███████ ███████ ██   ██     ██████  ██   ██    ██    ██   ██     ██   ██ ███████ ██   ████ ██   ██ ██      ██ ███████ ██   ██ 
```

# Mesh Data Renaming

## Overview
This Python script for Blender renames the mesh data of objects to match the names of the collections they are in. It helps organize and identify mesh data more easily in complex Blender projects.

[Capture vidéo du 22-12-2023 00:34:58.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/b2f59bf8-c593-49b3-b935-476c5670576a)

## Features
- Renames mesh data based on the parent collection's name.
- Adds an underscore and the object's name for uniqueness.

## Requirements
- Blender 2.80 or later.

## Usage
1. Open your Blender project.
2. Open a new or existing text editor within Blender.
3. Copy and paste the script into the text editor.
4. Run the script.

## Script
```python
import bpy

# Renames mesh data based on the collection name containing the object
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.users_collection:
        collection_name = obj.users_collection[0].name
        obj.data.name = collection_name + "_" + obj.name
```
