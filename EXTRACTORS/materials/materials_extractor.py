#      |               |                                 |
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  |                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    |
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#           |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#   |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                               |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#                |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#        |                                This script allows Blender to 
                
#                                extract one or every materials, turning it           |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#                     into python scripts that can be used with blender API for AI or else.

#              Script's origin : https://github.com/SECRET-GUEST/animation/tree/blender/EXTRACTORS
#                                   |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                    |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#           
#      |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                                |                                   |     |                  
#                   |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#              |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                 |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                         =)
                
#
#                                |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#              |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#      |                        |                                         |                                |
                
#
#                                                     !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#      |               |                                 !
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  !                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    !
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
import bpy
#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Settings:
material_name = ''  # Leave empty to export all materials
output_directory = ''  # Replace with your output directory

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

def safe_name(name):
    return name.replace(' ', '_')

def export_material(material, filepath):
    if not material.use_nodes or material.node_tree is None:
        print(f'Skipping {material.name} as it does not use nodes or has no node tree.')
        return  # Skip materials that do not use nodes or have no node tree

    with open(filepath, 'w') as file:
        file.write('import bpy\n\n')
        file.write(f"material = bpy.data.materials.new(name='{material.name}')\n")
        file.write("material.use_nodes = True\n")
        file.write("nodes = material.node_tree.nodes\n")
        file.write("links = material.node_tree.links\n\n")
        file.write("# Clear default nodes\n")
        file.write("for node in nodes:\n")
        file.write("    nodes.remove(node)\n\n")

        file.write("# Function to safely set attributes\n")
        file.write("def safe_set(node, prop_name, value):\n")
        file.write("    try:\n")
        file.write("        setattr(node, prop_name, value)\n")
        file.write("    except AttributeError:\n")
        file.write("        pass  # Property is read-only\n\n")

        for node in material.node_tree.nodes:
            safe_node_name = safe_name(node.name)
            file.write(f"# Create node {node.type}\n")
            file.write(f"{safe_node_name} = nodes.new(type='{node.bl_idname}')\n")
            file.write(f"{safe_node_name}.location = {node.location.x}, {node.location.y}\n")
            for prop_name in dir(node):
                if not prop_name.startswith("_"):  # Ignore private attributes
                    prop = getattr(node, prop_name)
                    if isinstance(prop, (str, int, float, bool)):
                        file.write(f"safe_set({safe_node_name}, '{prop_name}', {repr(prop)})\n")
                    elif isinstance(prop, (tuple, list)) and all(isinstance(v, (str, int, float, bool)) for v in prop):
                        file.write(f"safe_set({safe_node_name}, '{prop_name}', {repr(prop)})\n")
            for input in node.inputs:
                if input.type == 'VECTOR':
                    file.write(f"safe_set({safe_node_name}.inputs['{input.name}'], 'default_value', ({input.default_value[0]}, {input.default_value[1]}, {input.default_value[2]}))\n")
                elif input.type == 'VALUE':
                    file.write(f"safe_set({safe_node_name}.inputs['{input.name}'], 'default_value', {input.default_value})\n")
                elif input.type == 'RGBA':
                    file.write(f"safe_set({safe_node_name}.inputs['{input.name}'], 'default_value', ({input.default_value[0]}, {input.default_value[1]}, {input.default_value[2]}, {input.default_value[3]}))\n")
            file.write('\n')

        file.write("# Create links\n")
        for link in material.node_tree.links:
            safe_from_node_name = safe_name(link.from_node.name)
            safe_to_node_name = safe_name(link.to_node.name)
            from_socket_index = list(link.from_node.outputs).index(link.from_socket)
            to_socket_index = list(link.to_node.inputs).index(link.to_socket)
            file.write(f"links.new({safe_from_node_name}.outputs[{from_socket_index}], {safe_to_node_name}.inputs[{to_socket_index}])\n")
        file.write('\n')



# Ensure the output directory exists
bpy.ops.wm.path_open(filepath=output_directory)

if material_name:
    material = bpy.data.materials.get(material_name)
    if material:
        export_material(material, f'{output_directory}{safe_name(material_name)}.py')
    else:
        print(f'Material {material_name} not found')
else:
    for material in bpy.data.materials:
        export_material(material, f'{output_directory}{safe_name(material.name)}.py')
