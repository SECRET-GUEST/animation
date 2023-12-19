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
                
#                              make a new material from previous one baked fast           |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#                 https://github.com/SECRET-GUEST/animation/tree/blender/texturing/fast%20bake
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

# texture size
texture_width = 8192
texture_height = 8192

# names
baked_img_name = "BakedTexture"
new_material_name = "BakedMaterial"

#save 
save_image = True  # Set to False if you don't want to save the image
image_save_path = "//" + baked_img_name + ".png"  # Change this to your desired path

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |

# Check if an object is selected
if bpy.context.selected_objects:
    selected_obj = bpy.context.selected_objects[0]

    if selected_obj.type == 'MESH':
        # Switch to edit mode and apply Smart UV Project
        bpy.context.view_layer.objects.active = selected_obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.smart_project()
        bpy.ops.object.mode_set(mode='OBJECT')

        # Create a new image for baking
        baked_img = bpy.data.images.new(baked_img_name, width=texture_width, height=texture_height)

        # Prepare the material for baking
        mat = selected_obj.material_slots[0].material
        mat.use_nodes = True
        nodes = mat.node_tree.nodes

        # Create a Texture node and configure for baking
        tex_node = nodes.new('ShaderNodeTexImage')
        tex_node.image = baked_img
        tex_node.select = True
        nodes.active = tex_node

        # Set the render engine to Cycles for baking
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.bake_type = 'DIFFUSE'
        bpy.context.scene.render.bake.use_pass_direct = False
        bpy.context.scene.render.bake.use_pass_indirect = False

        # Prepare the object for baking
        for slot in selected_obj.material_slots:
            slot.material.node_tree.nodes.active = tex_node

        # Perform the bake
        bpy.ops.object.bake(type='DIFFUSE')

        # Create a new material with the baked texture
        new_mat = bpy.data.materials.new(name=new_material_name)
        new_mat.use_nodes = True
        bsdf = new_mat.node_tree.nodes.get('Principled BSDF')
        tex_image = new_mat.node_tree.nodes.new('ShaderNodeTexImage')
        tex_image.image = baked_img
        new_mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

        # Assign the new baked material to the object
        if selected_obj.data.materials:
            # Replace the existing material
            selected_obj.data.materials[0] = new_mat
        else:
            # Add the new material
            selected_obj.data.materials.append(new_mat)

        # Save the baked image if required
        if save_image:
            baked_img.filepath_raw = image_save_path
            baked_img.file_format = 'PNG'
            baked_img.save()

        # Clean up the nodes created for baking
        nodes.remove(tex_node)

else:
    print("No object selected.")
