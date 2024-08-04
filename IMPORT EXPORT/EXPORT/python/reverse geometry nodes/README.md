[![Blender](https://img.shields.io/badge/Blender-4.2-orange.svg)](https://www.blender.org/download/releases/4-2/)
[![Python](https://img.shields.io/badge/Python-3.11.7-blue.svg)](https://www.python.org/downloads/release/python-3117/)
```

██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗     ██████╗ ███████╗ ██████╗ ███╗   ███╗███████╗████████╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗      ██║  ███╗█████╗  ██║   ██║██╔████╔██║█████╗     ██║   ██████╔╝ ╚████╔╝ 
██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝      ██║   ██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗  ╚██╔╝  
██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗    ╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
                                                                                                                                    
```


# Blender Geometry Nodes Script Exporter

This repository contains two scripts for working with Geometry Nodes in Blender.


## Usage

### Script 1: Reverse Geometry Nodes

This script allows exporting Geometry Nodes from Blender to individual Python scripts which can be re-imported into Blender.

#### How to Use:

1. Open Blender and load your project.
2. Copy and paste the `reverse_geometry_nodes` script into Blender's text editor.
3. Modify the `save_path` setting at the beginning of the script to specify where the exported scripts will be saved.
4. Run the script.

Note: This script currently does not include input and output groups. This issue will be fixed in a future update.

### Script 2: Reverse Geometry Nodes Text

This script retrieves detailed information about the nodes and their connections in text format, which can be useful for debugging or other purposes.

#### How to Use:

1. Open Blender and load your project.
2. Copy and paste the `reverse_geometry_nodes_text` script into Blender's text editor.
3. Select the object with the Geometry Nodes modifier applied.
4. Run the script.

The script will generate a text file with detailed information about the nodes and their connections.

## Notes

- Ensure that the object you want to export or detail has a Geometry Nodes modifier applied.
- The exported files (from the `reverse_geometry_nodes` script) will be saved in the directory specified by `save_path`. Ensure that this directory exists or will be created.

---

J'espère que cela correspond maintenant à tes attentes.