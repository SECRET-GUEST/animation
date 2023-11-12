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
                
#        |                               This script allows Blender to  
                
#                                 wash your project from all unused things in          |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#               You can set whatever you want to remove  in settings but proceed with caution  !
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

# Set these variables to 'y' for yes or whatever else for no to choose what to clear
clear_caches = 'y'  
clear_keyframes = 'y' 
clear_unused_materials = 'y'  
clear_unused_textures = 'y'  
clear_unused_meshes = 'y'  
clear_unused_images = 'y'  
clear_unused_collections = 'y'  
clear_orphan_data = 'y'
clear_unused_uv_maps = 'y'
clear_unused_node_groups = 'y'


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                


def clear_simulation_caches():
    # Clear Particle System Caches
    for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type == 'PARTICLE_SYSTEM':
                modifier.particle_system.point_cache.frame_start = bpy.context.scene.frame_start

    # Clear Fluid Simulation Caches
    for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type == 'FLUID':
                if modifier.fluid_type == 'DOMAIN':
                    for cache in modifier.domain_settings.cache_settings.cache_file_format:
                        cache.use_external = False

    # Clear Smoke and Gas Simulation Caches
    for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type == 'FLUID':
                if modifier.fluid_type == 'DOMAIN' and modifier.domain_settings.domain_type == 'GAS':
                    for cache in modifier.domain_settings.cache_settings.cache_file_format:
                        cache.use_external = False

    # Clear Cloth and Soft Body Simulation Caches
    for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type in {'CLOTH', 'SOFT_BODY'}:
                modifier.point_cache.frame_start = bpy.context.scene.frame_start

    # Clear Rigid Body World Cache
    if bpy.context.scene.rigidbody_world:
        bpy.context.scene.rigidbody_world.point_cache.frame_start = bpy.context.scene.frame_start

def clear_all_keyframes():
    # Clear keyframes from all objects
    for obj in bpy.data.objects:
        if obj.animation_data:
            obj.animation_data_clear()

    # Clear keyframes from all materials
    for mat in bpy.data.materials:
        if mat.animation_data:
            mat.animation_data_clear()

    # Clear keyframes from all curves
    for curve in bpy.data.curves:
        if curve.animation_data:
            curve.animation_data_clear()

    # Clear keyframes from all cameras
    for cam in bpy.data.cameras:
        if cam.animation_data:
            cam.animation_data_clear()

    # Clear keyframes from all lights
    for light in bpy.data.lights:
        if light.animation_data:
            light.animation_data_clear()


def clear_unused_data_block(data_block):
    for item in data_block:
        if item.users == 0:
            data_block.remove(item)

def clear_orphaned_data():
    for block_type in [bpy.data.meshes, bpy.data.materials, bpy.data.textures, bpy.data.images, bpy.data.node_groups]:
        for block in block_type:
            if block.users == 0:
                block_type.remove(block)


def clear_uv_maps():
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.uv_layers:
            used_uv_maps = set()
            # Collect all UV Map names used in material slots
            for mat_slot in obj.material_slots:
                if mat_slot.material and mat_slot.material.use_nodes:
                    for node in mat_slot.material.node_tree.nodes:
                        if node.type == 'UVMAP':
                            used_uv_maps.add(node.uv_map)
            # Remove unused UV Maps
            for uv_map in obj.data.uv_layers:
                if uv_map.name not in used_uv_maps:
                    obj.data.uv_layers.remove(uv_map)


def clear_unused_nodes():
    # Clear unused node groups
    for group in bpy.data.node_groups:
        if group.users == 0:
            bpy.data.node_groups.remove(group)






# Apply the cleanup based on settings
if clear_unused_materials == 'y':
    clear_unused_data_block(bpy.data.materials)
    
if clear_unused_textures == 'y':
    clear_unused_data_block(bpy.data.textures)
    
if clear_unused_meshes == 'y':
    clear_unused_data_block(bpy.data.meshes)
    
if clear_unused_images == 'y':
    clear_unused_data_block(bpy.data.images)
    
if clear_unused_collections == 'y':
    clear_unused_data_block(bpy.data.collections)
    
if clear_orphan_data == 'y':
    clear_orphaned_data()
    
if clear_unused_uv_maps == 'y':
    clear_uv_maps()
    
if clear_unused_node_groups == 'y':
    clear_unused_nodes()

if clear_caches == 'y':
    clear_simulation_caches()

if clear_keyframes == 'y':
    clear_all_keyframes()
