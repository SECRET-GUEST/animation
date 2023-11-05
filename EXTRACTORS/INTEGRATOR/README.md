[![Blender](https://img.shields.io/badge/Blender-3.6-orange.svg)](https://www.blender.org/download/releases/3-6/)
[![Python](https://img.shields.io/badge/Python-3.10.13-blue.svg)](https://www.python.org/downloads/release/python-31013/)
```
██╗███╗   ██╗████████╗███████╗ ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██║████╗  ██║╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║██╔██╗ ██║   ██║   █████╗  ██║  ███╗██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║██║╚██╗██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║██║ ╚████║   ██║   ███████╗╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

# Executor and Importer 

This repository contains a script `inegrator.py` that allows you to either execute or import multiple Python scripts into Blender in a batch manner. This is useful when you have a collection of scripts that you want to run or have available within Blender's Text Editor all at once.

## Features

- Batch execute or import Python scripts located in a specified directory.
- Option to execute scripts immediately or just import them into Blender's Text Editor for manual execution later.

## How to Use

1. Clone or download this repository to your local machine.
2. Open Blender.
3. Go to the Text Editor view.
4. Create a new text data-block and paste the contents of `inegrator.py` into it.
5. Modify the `script_directory` variable at the top of the script to point to the directory containing the scripts you want to execute or import.
6. Modify the `execute_scripts` variable to `True` if you want to execute the scripts, or `False` if you want to import them into the Text Editor without executing.
7. Press the "Run Script" button to run the `inegrator.py` script.

The scripts in the specified directory will now either be executed or imported into Blender's Text Editor based on your setting.
