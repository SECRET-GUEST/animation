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
                
#                                generate clouds based on random shapes that             |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#               you can adjust in the parameters. https://www.artstation.com/artwork/qew98N
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

# Parameters
# Cloud:

cloud_size_x = 4  
cloud_size_y = 4 
noise_texture_scale = 4  
noise_texture_detail = 16 

# World environement:
use_world_sky = True  # Set background
background_color_hex = "#0060D4"  # Default is blue
# let or complete "" by the url of your image if you want a reflexion effect on the cloud.
skylink = ""
# You can find pictures here for free : https://www.artstation.com/artwork/qew98N

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
# Vérifier ou créer la collection 'clouds'
cloud_collection = bpy.data.collections.get("clouds")
if cloud_collection is None:
    cloud_collection = bpy.data.collections.new("clouds")
    bpy.context.scene.collection.children.link(cloud_collection)

# make the cube container then resize
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object
cube.name = "cloud"
cube.scale.x = cloud_size_x
cube.scale.y = cloud_size_y

# Add cube to new or older collection "clouds"
if cube.name not in cloud_collection.objects:
    cloud_collection.objects.link(cube)
    bpy.context.collection.objects.unlink(cube)

# New material
material = bpy.data.materials.new(name="pro_cloud")
material.use_nodes = True
nodes = material.node_tree.nodes
nodes.clear()  # Remove useless nodes

# Apply material to the cube
cube.data.materials.append(material)

# Material nodes
material_output = nodes.new(type="ShaderNodeOutputMaterial")
material_output.location = (1100, 0)
principled_volume = nodes.new(type="ShaderNodeVolumePrincipled")
principled_volume.location = (800, 0)
math_multiply = nodes.new(type="ShaderNodeMath")
math_multiply.location = (600, 0)
color_ramp = nodes.new(type="ShaderNodeValToRGB")
color_ramp.location = (300, 0)
gradient_texture = nodes.new(type="ShaderNodeTexGradient")
gradient_texture.location = (100, 0)
mapping = nodes.new(type="ShaderNodeMapping")
mapping.location = (-100, 0)
math_vector = nodes.new(type="ShaderNodeVectorMath")
math_vector.location = (-300, 0)
texture_coordinate = nodes.new(type="ShaderNodeTexCoord")
texture_coordinate.location = (-500, 280)
noise_texture = nodes.new(type="ShaderNodeTexNoise")
noise_texture.location = (-500, 0)
object_info = nodes.new(type="ShaderNodeObjectInfo")
object_info.location = (-700, 0)

# Nodes values
principled_volume.inputs['Density'].default_value = 1
math_multiply.operation = 'MULTIPLY'
math_multiply.inputs[1].default_value = 500
gradient_texture.gradient_type = 'QUADRATIC_SPHERE'
mapping.inputs['Location'].default_value = (-4, -4, -4)
mapping.inputs['Scale'].default_value = (4, 4, 4)
noise_texture.noise_dimensions = '4D'
noise_texture.inputs['Scale'].default_value = noise_texture_scale
noise_texture.inputs['Detail'].default_value = noise_texture_detail

# Nodes links
material.node_tree.links.new(material_output.inputs['Volume'], principled_volume.outputs['Volume'])
material.node_tree.links.new(principled_volume.inputs['Density'], math_multiply.outputs['Value'])
material.node_tree.links.new(math_multiply.inputs[0], color_ramp.outputs['Color'])
material.node_tree.links.new(color_ramp.inputs['Fac'], gradient_texture.outputs['Color'])
material.node_tree.links.new(gradient_texture.inputs['Vector'], mapping.outputs['Vector'])
material.node_tree.links.new(mapping.inputs['Vector'], math_vector.outputs['Vector'])
material.node_tree.links.new(math_vector.inputs[0], texture_coordinate.outputs['Generated'])
material.node_tree.links.new(math_vector.inputs[1], noise_texture.outputs['Color'])
material.node_tree.links.new(noise_texture.inputs['W'], object_info.outputs['Random'])

# Convert hex to RGB for the world
background_color_rgb = tuple(int(background_color_hex.lstrip('#')[i:i+2], 16) / 255.0 for i in (0, 2, 4))

# Configure sky shader if use_world_sky is True
if use_world_sky:
    # Ensure we're working with the World
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world

    # Get or create a new node tree for the World
    world.use_nodes = True
    nodes = world.node_tree.nodes
    nodes.clear()  # Clear all existing nodes

    # 1. Create Texture Coordinate and Mapping nodes
    tex_coord = nodes.new(type="ShaderNodeTexCoord")
    tex_coord.location = (0, 0)
    
    mapping = nodes.new(type="ShaderNodeMapping")
    mapping.location = (200, 0)
    bpy.context.scene.world.node_tree.links.new(tex_coord.outputs["Generated"], mapping.inputs["Vector"])

    if skylink is None or skylink == "":
        # skylink is None, use single background setup
        background = nodes.new(type="ShaderNodeBackground")
        background.location = (600, 0)
        background.inputs[0].default_value = (*background_color_rgb, 1)  # Set the color from the hex value
        
        world_output = nodes.new(type="ShaderNodeOutputWorld")
        world_output.location = (800, 0)
        bpy.context.scene.world.node_tree.links.new(background.outputs["Background"], world_output.inputs["Surface"])
        
    else:  
        # skylink is provided, use reflection setup
        env_texture = nodes.new(type="ShaderNodeTexEnvironment")
        env_texture.image = bpy.data.images.load(filepath=skylink)
        env_texture.location = (400, 0)
        bpy.context.scene.world.node_tree.links.new(mapping.outputs["Vector"], env_texture.inputs["Vector"])

        background1 = nodes.new(type="ShaderNodeBackground")
        background1.location = (600, 100)
        
        background2 = nodes.new(type="ShaderNodeBackground")
        background2.location = (600, -100)
        background2.inputs[0].default_value = (*background_color_rgb, 1)
        
        light_path = nodes.new(type="ShaderNodeLightPath")
        light_path.location = (600, -300)
        
        bpy.context.scene.world.node_tree.links.new(env_texture.outputs["Color"], background1.inputs["Color"])
        
        mix_shader = nodes.new(type="ShaderNodeMixShader")
        mix_shader.location = (800, 0)
        bpy.context.scene.world.node_tree.links.new(light_path.outputs["Is Camera Ray"], mix_shader.inputs["Fac"])
        bpy.context.scene.world.node_tree.links.new(background1.outputs["Background"], mix_shader.inputs[1])
        bpy.context.scene.world.node_tree.links.new(background2.outputs["Background"], mix_shader.inputs[2])
        
        world_output = nodes.new(type="ShaderNodeOutputWorld")
        world_output.location = (1000, 0)
        bpy.context.scene.world.node_tree.links.new(mix_shader.outputs["Shader"], world_output.inputs["Surface"])
        
