#   |               |                                 |
                
#               |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#        |                                  |                                     |
                
#               |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#|                          |                       |                    |
#        |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#   |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                   |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#        |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#               |                     |
#|                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#        |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#|         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                            |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#             |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#     |                                This script allows Blender to 
                
#                               generate a cables crawling on the ground              |                                           |               |                                           |               |                                           |                    |                                           |
                
#                        /                      |    v    |                    \
#                in half a circle, with some settings like to make it fall from the top 
#                                |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                 |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#        
#   |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                             |                                   |     |                  
#                |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#           |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#              |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                      =)
                
#
#                             |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#           |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#   |                        |                                         |                                |
                
#
#                                                  !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#   |               |                                 !
                
#               |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#        |                                  !                                     |
                
#               |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#|                          |                       |                    !
#        |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
             
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|

#You don't have to import with pip, just paste the code in blender               
#Settings are in the end of script

import bpy
import math
import random
from mathutils import Vector





#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   

 #Here you can change the value if you need 
  
#Delete all existing objects in the scene (uncomment if you need)
#bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.delete(use_global=False)

#Paramètres ajustables
num_cables = 10  #number of cables
radius = 2.0     #radius of the circle
height = 1.0     #height of the cables column 
random_seed = 42 #random seed for cable diameters and undulations
 
collection_name = "cables" # change it to name the new collection






#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
               
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3



#Function to create a material with a given name and color
def create_material(name, color):
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()

    #Create a diffuse shader node and set its color
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    diffuse.inputs['Color'].default_value = color

    #Create an output node and link the diffuse shader to it
    output = nodes.new(type='ShaderNodeOutputMaterial')
    links.new(diffuse.outputs['BSDF'], output.inputs['Surface'])
    
    return material

#Function to create a cable with a given radius, height, angle, name, diameter, and material
def create_cable(radius, height, angle, cable_name, diameter, material):
    points = []

    #Define the start and end points of the cable
    start_point = Vector((radius * math.cos(angle), radius * math.sin(angle), 0))
    end_point = Vector((radius * math.cos(angle), radius * math.sin(angle), height))

    #Define some intermediate points for the cable using the midpoint formula
    points.append(start_point)
    points.append((end_point - start_point) / 2)
    points.append(end_point)

    #Create a new curve data object
    curve_data = bpy.data.curves.new(cable_name, 'CURVE')
    curve_data.dimensions = '3D'

    #Add a new spline to the curve data object and set its control points
    spline = curve_data.splines.new('BEZIER')
    spline.bezier_points.add(len(points) - 1)

    for i, point in enumerate(points):
        spline.bezier_points[i].co = point
        spline.bezier_points[i].handle_right_type = 'AUTO'
        spline.bezier_points[i].handle_left_type = 'AUTO'
    
    curve_data.resolution_u = 12

    #Create a new object from the curve data object and add it to the scene
    cable = bpy.data.objects.new(cable_name, curve_data)
    bpy.context.collection.objects.link(cable)

    #Set the bevel depth and material of the cable object
    cable.data.bevel_depth = diameter
    cable.data.materials.append(material)

    return cable



#Create a new collection named with the name of the varibale in the settings
collectioname = bpy.data.collections.new(collection_name)
bpy.context.scene.collection.children.link(collectioname)



#Function to create multiple cables with a given number of cables, radius, height, and random seed
def create_wires(num_cables, radius, height, random_seed):
    random.seed(random_seed)

    #Create a material to be used for all the cables
    material = create_material("blackwire", (0, 0, 0, 1))

    #Create a new cable for each specified number of cables
    for i in range(num_cables):
        angle = 2 * math.pi * i / num_cables
        cable_name = f"Cable_{i+1}"
        diameter = random.uniform(0.01, 0.05)
        cable = create_cable(radius, height, angle, cable_name, diameter, material)

        collectioname.objects.link(cable)
        bpy.context.collection.objects.unlink(cable)


#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3
   

create_wires(num_cables, radius, height, random_seed)
