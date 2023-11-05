[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
███╗   ███╗ █████╗ ████████╗███████╗██████╗ ██╗ █████╗ ██╗     ███████╗    ██████╗     ██████╗ ██╗   ██╗
████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║██╔══██╗██║     ██╔════╝    ╚════██╗    ██╔══██╗╚██╗ ██╔╝
██╔████╔██║███████║   ██║   █████╗  ██████╔╝██║███████║██║     ███████╗     █████╔╝    ██████╔╝ ╚████╔╝ 
██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██║██╔══██║██║     ╚════██║    ██╔═══╝     ██╔═══╝   ╚██╔╝  
██║ ╚═╝ ██║██║  ██║   ██║   ███████╗██║  ██║██║██║  ██║███████╗███████║    ███████╗    ██║        ██║   
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝    ╚═╝        ╚═╝   
```


# Blender Material Extractor

This script allows exporting materials from Blender to individual Python scripts which can be re-imported into Blender.

## Usage

1. Open Blender and load your project.
2. Copy and paste the `material_extractor` script into Blender's text editor.
3. Modify the `material_name` and `output_directory` settings as needed:
   - `material_name`: The name of the material you wish to export. Leave as an empty string (`''`) or `None` to export all materials.
   - `output_directory`: The directory where the exported scripts will be saved.
4. Run the script.

## Settings:

- `material_name`: Specify the name of the material you want to export. Leave it as an empty string (`''`) or `None` to export all materials in the project.
- `output_directory`: Specify the path to the directory where you want to save the exported scripts.

## Notes

- If you specify a `material_name`, only the corresponding material will be exported. Otherwise, all materials will be exported, each to its own file.
- The exported files will be saved in the directory specified by `output_directory`. Ensure that this directory exists or will be created.
- The names of the exported files will be based on the material names, with spaces replaced by underscores (`_`).
