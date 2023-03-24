BLENDER 3.4 | Python API script
```
███████╗ ██████╗ █████╗ ████████╗████████╗███████╗██████╗ ███████╗██╗   ██╗██████╗ ███████╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝
███████╗██║     ███████║   ██║      ██║   █████╗  ██████╔╝███████╗██║   ██║██████╔╝█████╗  
╚════██║██║     ██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗╚════██║██║   ██║██╔══██╗██╔══╝  
███████║╚██████╗██║  ██║   ██║      ██║   ███████╗██║  ██║███████║╚██████╔╝██║  ██║██║     
╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     
                                                                                           
```

![0](https://user-images.githubusercontent.com/92639080/227415938-a9d36c28-de02-441a-b488-263681bd02e0.gif)


# Blender script to generate random Parts on character/object surface

This script is designed for use in the Blender 3D modeling and animation software. It generates mechanical parts on the surface of a character object using a specified list of part names. The generated parts can be symmetrical or asymmetrical, depending on the user's preference.

The script consists of several functions:

- `create_collection(name, parent_collection=None)`: Creates a new collection with the specified name and optional parent collection. If no parent collection is specified, the new collection is linked to the scene collection.

- `merge_objects_in_collection(target_collection, collection_name, new_object_name)`: Merges all mesh objects in the collection with the specified name into a new mesh object with the specified name. The new object is then linked to the target collection.

- `create_mech_part(collection, part_name, location, rotation)`: Creates a new mechanical part object with the specified part name, location, and rotation. If the part name is already a collection, the script uses `merge_objects_in_collection()` to merge all objects in the collection into a single object.

- `get_character_bvh_tree(character)`: Generates a BVHTree from the specified character object, which is used to efficiently test for intersection between rays and the character's mesh.

- `get_surface_point(character, bvh_tree)`: Gets a random surface point on the specified character object using the provided BVHTree to test for intersection between rays and the character's mesh.

- `generate_mech_parts(character, part_names, num_parts, use_symmetry)`: Generates a specified number of mechanical parts on the surface of the specified character object. The generated parts are created in a new collection and returned as a list.

To use the script, simply specify the character object, a list of part names, the number of parts to generate, and whether to use symmetry. The script will then generate the specified number of mechanical parts on the surface of the character object using the specified part names and return the generated parts as a list.

Example usage:

```python
character = bpy.data.objects['p2']
part_names = ('1', 'Cable', 'wire')
num_parts = 5
use_symmetry = True
mech_parts = generate_mech_parts(character, part_names, num_parts, use_symmetry)

![pic0028](https://user-images.githubusercontent.com/92639080/227416016-489fce69-db28-4dd8-a8c3-65548ed2c028.png)

