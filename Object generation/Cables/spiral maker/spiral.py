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
                
#                                  make a spiral of cable or not that you can              |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#                 easily customize by set the parameters you want, all is explaned in comments
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
import math


#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Parameters
number_of_spirals = 3  # Number of spirals
height = 20  # Height of the spiral
revolutions = 1  # Number of revolutions
radius = 0.5  # Initial radius of the spiral
lenght_between_spirals = 0.1  # Tighten spiral to be closer to the center

create_pipes = True  # False to not convert spirals to pipes

# Extension Parameters
extend_outward = True  # False to not extend
extend_inward = True  

extension_length = 5  # Length of the extension
skin_thickness = 0.1  # Thickness of the pipe
subdiv_levels = 1  # Subdivision level



#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

def create_spirals():
    if "Spirale" not in bpy.data.collections:
        spirale_collection = bpy.data.collections.new("Spirale")
        bpy.context.scene.collection.children.link(spirale_collection)
    else:
        spirale_collection = bpy.data.collections["Spirale"]

    # Calculate extension angle based on the number of spirals
    extension_angle = 120 if number_of_spirals < 3 else 360 / number_of_spirals

    for i in range(number_of_spirals):
        # Increase radius based on the number of spirals
        # If the number of spirals is greater than 3, increase the initial radius by 0.1 for each additional spiral.
        # This separates the spirals from each other to avoid overlap.
        spiral_radius = radius + (i - 2) * lenght_between_spirals if i >= 3 else radius
        
        curve_data = bpy.data.curves.new(name=f"Spiral{i}", type='CURVE')
        curve_data.dimensions = '3D'
        curve_obj = bpy.data.objects.new(f"Spiral{i}", curve_data)
        spirale_collection.objects.link(curve_obj)
        polyline = curve_data.splines.new('POLY')
        polyline.points.add(height + 1)
        
        for j, point in enumerate(polyline.points):
            # Calculate the coordinates x and y using the angle and radius
            # The terms i * 2 * math.pi / number_of_spirals create an angular offset
            # for each spiral, allowing them to be separated.
            angle = 2 * math.pi * revolutions * j / height
            z = j
            x = spiral_radius * math.cos(angle + i * 2 * math.pi / number_of_spirals)
            y = spiral_radius * math.sin(angle + i * 2 * math.pi / number_of_spirals)
            
            # Adjust the coordinates for the extension
            # If extending outward is enabled and we are at the last point,
            # calculate a new angle to stretch the point outward.
            if extend_outward and j == height + 1:
                angle_extension = angle + i * 2 * math.pi / number_of_spirals + math.radians(extension_angle * i)
                x = extension_length * math.sin(angle_extension)
                y = extension_length * math.cos(angle_extension)
                
            # Extension from the origin
            elif extend_inward and j == 0:
                angle_extension = angle + i * 2 * math.pi / number_of_spirals + math.radians(extension_angle * i)
                x = extension_length * math.sin(angle_extension)
                y = extension_length * math.cos(angle_extension)
            
            # Point assignment
            point.co = (x, y, z, 1)


create_spirals()

# If create_pipes is True, convert spirals to pipes
if create_pipes:
    # Ensure that the "Spirale" collection is in the active View Layer
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children['Spirale']

    # Select all the spirals
    bpy.ops.object.select_all(action='DESELECT')
    for spiral_name in [f"Spiral{i}" for i in range(number_of_spirals)]:
        bpy.data.objects[spiral_name].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['Spiral0']

    # Convert curves to mesh
    bpy.ops.object.convert(target='MESH')

    # Add a skin modifier and a subdivision surface modifier
    for i in range(number_of_spirals):
        obj = bpy.data.objects[f"Spiral{i}"]
        skin_modifier = obj.modifiers.new(name="Skin", type='SKIN')
        # Adjust the parameters of the skin modifier if necessary
        skin_modifier.use_smooth_shade = True  # For example
        skin_modifier.branch_smoothing = 1  # For example
        
        # Add a subdivision surface modifier to smooth the mesh
        subdiv_modifier = obj.modifiers.new(name="Subdivision", type='SUBSURF')
        subdiv_modifier.levels = subdiv_levels  # Adjust the subdivision level if necessary
