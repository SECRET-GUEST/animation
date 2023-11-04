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
import random
#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Parameters
# Cloud:
num_metaballs = 15  # Number of metaballs
metaball_size = 3  # Base size of metaballs
distance = 3  # Distance between metaballs

# Volume:
voxel_amount = 108  # Voxel Amount parameter for Mesh to Volume modifier
strength = 2.0  # Strength parameter for Volume Displace modifier
texture_type = 'SOFT'  # Texture type: 'HARD' or 'SOFT'
cloud_texture_size = 2  # Texture size

# World environement:
use_world_sky = True  # Only set an image for the world background
use_world_reflexion = True # Set background + a reflective image 
background_color_hex = "#0060D4"  # Default is blue
# Link to the environment image to have a reflexion
skylink = ""


# Lights:
spotlight_cloud = True  # Create a spotlight
spotlight_distance = 20.0  # Distance of the spotlight
lumens = 20000  # Power of the spotlight


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                


# Check or create 'clouds' collection
cloud_collection = bpy.data.collections.get("clouds")
if cloud_collection is None:
    cloud_collection = bpy.data.collections.new("clouds")
    bpy.context.scene.collection.children.link(cloud_collection)

# Create metaballs
bpy.ops.object.select_all(action='DESELECT')  # Deselect all
for i in range(num_metaballs):
    bpy.ops.object.metaball_add(type='BALL', radius=random.uniform(metaball_size * 0.9, metaball_size * 1.1))
    metaball = bpy.context.active_object
    metaball.location.x = random.uniform(-distance, distance)
    metaball.location.y = random.uniform(-distance, distance)
    metaball.location.z = random.uniform(-distance, distance)
    cloud_collection.objects.link(metaball)
    bpy.context.collection.objects.unlink(metaball)

# Convert metaballs to mesh and rename
bpy.ops.object.select_all(action='DESELECT')  # Deselect all
for obj in cloud_collection.objects:
    obj.select_set(True)
bpy.ops.object.convert(target='MESH')
cloud_mesh = bpy.context.active_object
existing_clouds = [obj for obj in bpy.data.objects if obj.name.startswith("Cloud")]
cloud_mesh.name = f"Cloud{len(existing_clouds) + 1}"

# Create transparency material and assign to cloud mesh
transparency_material = bpy.data.materials.get("transparency")
if transparency_material is None:
    transparency_material = bpy.data.materials.new(name="transparency")
    transparency_material.use_nodes = True
    nodes = transparency_material.node_tree.nodes
    bsdf_node = nodes.get("Principled BSDF")
    bsdf_node.inputs['Alpha'].default_value = 0
cloud_mesh.data.materials.append(transparency_material)

# Create and configure empty volume
bpy.ops.object.volume_add()
volume = bpy.context.active_object
volume.name = "CloudVolume"
cloud_collection.objects.link(volume)
bpy.context.collection.objects.unlink(volume)

# Add and configure modifiers
volume.modifiers.new("MeshToVolume", 'MESH_TO_VOLUME')
volume.modifiers["MeshToVolume"].object = cloud_mesh
volume.modifiers["MeshToVolume"].voxel_amount = voxel_amount
volume.modifiers.new("VolumeDisplace", 'VOLUME_DISPLACE')
volume.modifiers["VolumeDisplace"].strength = strength

# Configure texture
texture = bpy.data.textures.get("Vapor")
if texture is None:
    texture = bpy.data.textures.new("Vapor", type='CLOUDS')
    texture.intensity = 1.0
    texture.contrast = 1.0
    texture.hard = 0 if texture_type == 'SOFT' else 1
    texture.size = cloud_texture_size
volume.modifiers["VolumeDisplace"].texture = texture


# Create spotlight if spotlight_cloud is True
if spotlight_cloud:
    bpy.ops.object.light_add(type='SPOT', location=(0, 0, spotlight_distance))
    spotlight = bpy.context.active_object
    spotlight.data.energy = lumens
    lights_collection = bpy.data.collections.get("lights")
    if lights_collection is None:
        lights_collection = bpy.data.collections.new("lights")
        bpy.context.scene.collection.children.link(lights_collection)
    spotlight_clouds_collection = lights_collection.children.get("spotlight_clouds")
    if spotlight_clouds_collection is None:
        spotlight_clouds_collection = bpy.data.collections.new("spotlight_clouds")
        lights_collection.children.link(spotlight_clouds_collection)
    spotlight_clouds_collection.objects.link(spotlight)
    bpy.context.collection.objects.unlink(spotlight)



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

    # 2. Create an Environment Texture node
    env_texture = nodes.new(type="ShaderNodeTexEnvironment")
    env_texture.image = bpy.data.images.load(filepath=skylink)
    env_texture.location = (400, 0)
    bpy.context.scene.world.node_tree.links.new(mapping.outputs["Vector"], env_texture.inputs["Vector"])

    if use_world_reflexion:
        # 3. Create two Background nodes and a Light Path node
        background1 = nodes.new(type="ShaderNodeBackground")
        background1.location = (600, 100)

        background2 = nodes.new(type="ShaderNodeBackground")
        background2.location = (600, -100)
        background2.inputs[0].default_value = (*background_color_rgb, 1)

        light_path = nodes.new(type="ShaderNodeLightPath")
        light_path.location = (600, -300)

        # Connect the Environment Texture's color output to the first Background node's color input
        bpy.context.scene.world.node_tree.links.new(env_texture.outputs["Color"], background1.inputs["Color"])

        # 4. Create a Mix Shader node
        mix_shader = nodes.new(type="ShaderNodeMixShader")
        mix_shader.location = (800, 0)
        bpy.context.scene.world.node_tree.links.new(light_path.outputs["Is Camera Ray"], mix_shader.inputs["Fac"])
        bpy.context.scene.world.node_tree.links.new(background1.outputs["Background"], mix_shader.inputs[1])
        bpy.context.scene.world.node_tree.links.new(background2.outputs["Background"], mix_shader.inputs[2])

        # 5. Create a World Output node
        world_output = nodes.new(type="ShaderNodeOutputWorld")
        world_output.location = (1000, 0)
        bpy.context.scene.world.node_tree.links.new(mix_shader.outputs["Shader"], world_output.inputs["Surface"])
        
    else:
        # Single background setup (no reflection)
        background = nodes.new(type="ShaderNodeBackground")
        background.location = (600, 0)
        bpy.context.scene.world.node_tree.links.new(env_texture.outputs["Color"], background.inputs["Color"])
        
        # Create a World Output node
        world_output = nodes.new(type="ShaderNodeOutputWorld")
        world_output.location = (800, 0)
        bpy.context.scene.world.node_tree.links.new(background.outputs["Background"], world_output.inputs["Surface"])
