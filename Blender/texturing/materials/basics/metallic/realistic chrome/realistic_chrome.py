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
#                |                           /                     \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#        |                          This script provides an ultra-realistic 
                
#                    chrome material for Blender objects using only native Blender shaders.             |                                           |               |                                           |               |                                           |                    |                                           |
# 
#                     /                           |    v    |                            \

#        It takes into account subtle imperfections and reflections to achieve a high level of realism. 
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

#You don't have to import with pip, just paste the code in blender     

import bpy

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

def apply_custom_chrome_material(obj):
    # 1. Create a new material named "chrome". If it already exists, append a number to its name.
    material_name = "chrome"
    i = 1
    while bpy.data.materials.get(material_name):
        material_name = "chrome" + str(i)
        i += 1
    chrome_material = bpy.data.materials.new(name=material_name)
    chrome_material.use_nodes = True
    nodes = chrome_material.node_tree.nodes
    nodes.clear()  # Clear all nodes to start fresh

    # 2. Create a Noise Texture shader and two Musgrave Textures in a column.
    noise_texture = nodes.new(type="ShaderNodeTexNoise")
    noise_texture.location = (-600, 200)
    musgrave1 = nodes.new(type="ShaderNodeTexMusgrave")
    musgrave1.location = (-600, 0)
    musgrave2 = nodes.new(type="ShaderNodeTexMusgrave")
    musgrave2.location = (-600, -200)

    # 2 bis. Set the properties of the Musgrave Textures and Noise Texture.
    musgrave1.inputs["Scale"].default_value = 10
    musgrave1.inputs["Detail"].default_value = 8
    musgrave1.inputs["Dimension"].default_value = 0.5

    musgrave2.inputs["Scale"].default_value = 35
    musgrave2.inputs["Detail"].default_value = 6
    musgrave2.inputs["Dimension"].default_value = 0.12

    noise_texture.inputs["Scale"].default_value = 18
    noise_texture.inputs["Detail"].default_value = 3

    # 3. Create three ColorRamp nodes to the left of the previous column.
    color_ramp_noise = nodes.new(type="ShaderNodeValToRGB")
    color_ramp_noise.location = (-800, 200)
    color_ramp_musgrave1 = nodes.new(type="ShaderNodeValToRGB")
    color_ramp_musgrave1.location = (-800, 0)
    color_ramp_musgrave2 = nodes.new(type="ShaderNodeValToRGB")
    color_ramp_musgrave2.location = (-800, -200)

    # 3 bis. Set the properties of the ColorRamp nodes.
    color_ramp_noise.color_ramp.elements[0].position = 0.3

    color_ramp_musgrave1.color_ramp.elements[0].position = 0.3
    color_ramp_musgrave1.color_ramp.elements[0].color = [0.04, 0.04, 0.04, 1]
    color_ramp_musgrave1.color_ramp.elements[1].color = [0.5, 0.5, 0.5, 1]

    color_ramp_musgrave2.color_ramp.elements[0].position = 0.8

    # 4. Connect the shaders to the ColorRamp nodes.
    chrome_material.node_tree.links.new(noise_texture.outputs["Fac"], color_ramp_noise.inputs[0])
    chrome_material.node_tree.links.new(musgrave1.outputs["Fac"], color_ramp_musgrave1.inputs[0])
    chrome_material.node_tree.links.new(musgrave2.outputs["Fac"], color_ramp_musgrave2.inputs[0])

    # 5. Create a Bump node and set its properties.
    bump = nodes.new(type="ShaderNodeBump")
    bump.location = (-400, 200)
    bump.inputs["Strength"].default_value = 0.35
    bump.inputs["Distance"].default_value = 0.15
    chrome_material.node_tree.links.new(color_ramp_noise.outputs["Color"], bump.inputs["Height"])

    # 6. Create a Principled BSDF shader and set its properties.
    principled_bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    principled_bsdf.location = (-200, 0)
    principled_bsdf.inputs["Metallic"].default_value = 1
    chrome_material.node_tree.links.new(color_ramp_musgrave1.outputs["Color"], principled_bsdf.inputs["Roughness"])
    chrome_material.node_tree.links.new(bump.outputs["Normal"], principled_bsdf.inputs["Normal"])

    # 7. Create a Material Output node and connect the Principled BSDF to it.
    material_output = nodes.new(type="ShaderNodeOutputMaterial")
    material_output.location = (0, 0)
    chrome_material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

    # 8. Create a Displacement node and set its properties.
    displacement = nodes.new(type="ShaderNodeDisplacement")
    displacement.location = (-400, -200)
    chrome_material.node_tree.links.new(color_ramp_musgrave2.outputs["Color"], displacement.inputs["Scale"])
    chrome_material.node_tree.links.new(displacement.outputs["Displacement"], material_output.inputs["Displacement"])

    # 9. Apply the material to the selected object or face.
    if obj.data.materials:
        obj.data.materials[0] = chrome_material
    else:
        obj.data.materials.append(chrome_material)

# Get the currently selected object
selected_obj = bpy.context.active_object

# Apply the custom chrome material to the selected object
apply_custom_chrome_material(selected_obj)
