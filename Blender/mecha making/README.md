BLENDER | Python API script
```
███╗   ███╗███████╗ ██████╗██╗  ██╗ █████╗     ██████╗  █████╗ ██████╗ ████████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
████╗ ████║██╔════╝██╔════╝██║  ██║██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║█████╗  ██║     ███████║███████║    ██████╔╝███████║██████╔╝   ██║       ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██╔══╝  ██║     ██╔══██║██╔══██║    ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║███████╗╚██████╗██║  ██║██║  ██║    ██║     ██║  ██║██║  ██║   ██║       ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

# Description

This script generates a number of mech parts at random surface locations on a character object in Blender, and optionally creates mirrored copies of the parts. 

The parts are selected from a list of object names provided as input.

# Features

- Randomly places a set of mech parts on the surface of a character object in Blender
- Supports duplication of objects to create mirrored copies along the x-axis
- Uses a BVH tree for fast nearest surface point lookup
- Supports a range of input parameters including object names, number of parts, and symmetry flag
