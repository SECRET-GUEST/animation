[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)

```
██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗    ███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗
██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║       █████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║   
██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║       ██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║       ███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
```

# Blender Data Extractor and Integrator

This repository contains a collection of Python scripts designed for Blender, aiming at extracting data, into Python scripts for example.

## Contents
1. **EXPORT**:
   - Extract data in multiple formats.

2. **IMPORT**:
   - Import data as 3D, batch, ...

## Usage
The scripts are meant to be run within Blender's Text Editor view. Copy and paste the desired script into a new text data-block in the Text Editor, update any necessary variables, and click "Run Script" to execute.

For detailed instructions on using each script, refer to the README files located in the respective folders.

## Purpose
The primary goal of these scripts is to bridge the gap between Blender and external projects or AI training pipelines. By extracting material data into Python scripts, it becomes straightforward to integrate this data into other environments. Additionally, the integrator script aids in automating the execution of multiple scripts, saving time and ensuring a streamlined workflow.

## Notes
- Ensure you have the necessary read/write permissions for the specified directories.
- Exercise caution when executing scripts, they have no limitations.
