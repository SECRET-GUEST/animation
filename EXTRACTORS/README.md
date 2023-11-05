[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗    ████████╗ ██████╗     ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
█████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║          ██║   ██║   ██║    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║          ██║   ██║   ██║    ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║          ██║   ╚██████╔╝    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝          ╚═╝    ╚═════╝     ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

# Blender Data Extractor and Integrator

This repository contains a collection of Python scripts designed for Blender, aiming at extracting data, particularly materials, into Python scripts. The extracted data can be easily integrated into other projects or used for training Artificial Intelligence (AI) models. Additionally, an integrator script is provided to execute all scripts in a specified directory within Blender in sequence.

[Capture vidéo du 05-11-2023 04:02:59.webm](https://github.com/SECRET-GUEST/animation/assets/92639080/b929d892-b3bd-4084-895b-12da863f7981)

## Contents

1. **Material Extractor**:
   - The `material_extractor.py` script extracts data from specified materials or all materials within a Blender project.
   - Extracted data is saved into separate Python scripts for each material.
   - The scripts are stored in a specified output directory.
   - Refer to the `material_extractor/README.md` for usage details.

2. **Integrator**:
   - The `integrator.py` script reads and executes all Python scripts located in a specified directory within Blender.
   - This script facilitates batch execution of scripts within Blender.
   - Refer to the `integrator/README.md` for usage details.

## Usage

The scripts are meant to be run within Blender's Text Editor view. Copy and paste the desired script into a new text data-block in the Text Editor, update any necessary variables, and click "Run Script" to execute.

For detailed instructions on using each script, refer to the README files located in the respective folders (`material_extractor` and `integrator`).

## Purpose

The primary goal of these scripts is to bridge the gap between Blender and external projects or AI training pipelines. By extracting material data into Python scripts, it becomes straightforward to integrate this data into other environments. Additionally, the integrator script aids in automating the execution of multiple scripts, saving time and ensuring a streamlined workflow.

## Notes

- Ensure you have the necessary read/write permissions for the specified directories.
- Exercise caution when executing scripts, especially from untrusted sources, to avoid unintended consequences.
