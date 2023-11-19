#    |               |                                 |
                
#                |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#         |                                  |                                     |
                
#                |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
# |                          |                       |                    |
#         |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#    |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                    |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#         |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                |                     |
# |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#         |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
# |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                             |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#              |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#      |                                This script allows Blender to 
                
#                           generate papers in the ground of your old laboratory           |                                           |               |                                           |               |                                           |                    |                                           |
                
#                         /                      |    v    |                    \
#              or whatever else you're building. You can adjust almost everything in settings
#                                 |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                  |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#         
#    |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                              |                                   |     |                  
#                 |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#            |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#               |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                       =)
                
#
#                              |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#            |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#    |                        |                                         |                                |
                
#
#                                                   !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#    |               |                                 !
                
#                |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#         |                                  !                                     |
                
#                |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
# |                          |                       |                    !
#         |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
             
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|

#You don't have to import with pip, just paste the code in blender               


import bpy
import bmesh
import random
import math


#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#Here you can set the ratio you want for all your selected objects 
  

num_papers = 50             #Number of papers to generate
circle_diameter = 5         #Diameter of the circle
paper_thickness = 0.001     #Thickness of the papers
uniform_size = True         #Set to True for all papers to have the same size and shape
random_tilt = False         #Set to True for papers to have a random tilt
random_rotation = True      #Set to True for papers to have a random rotation (uniform_size must be True and random_tilt must be False)

collection_name = "papers" #Name of the collection





#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST :3


#Function to create a paper with folds
def create_paper(x, y, z, width, height, thickness, collection):
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
    paper = bpy.context.active_object
    paper.scale = (width / 2, height / 2, thickness)
    paper.name = "Paper"

    #Add folds
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=4)
    bpy.ops.object.mode_set(mode='OBJECT')

    #Modify vertices to create folds
    bm = bmesh.new()
    bm.from_mesh(paper.data)
    for vert in bm.verts:
        vert.co.z += random.uniform(-thickness / 2, thickness / 2)
    bm.to_mesh(paper.data)
    bm.free()

    #Add slight rotation
    if random_tilt:
        paper.rotation_euler = (random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2))
    elif random_rotation:
        paper.rotation_euler = (0, 0, random.uniform(0, 2 * math.pi))

    #Move paper to the specified collection
    bpy.context.view_layer.active_layer_collection.collection.objects.unlink(paper)
    collection.objects.link(paper)

    return paper

#Function to generate a random point in a circle
def random_point_in_circle(radius):
    angle = random.uniform(0, 2 * math.pi)
    r = math.sqrt(random.uniform(0, radius ** 2))
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return x, y

#Create a new collection named with the name of the varibale in the settings
collectioname = bpy.data.collections.new(collection_name)
bpy.context.scene.collection.children.link(collectioname)

if uniform_size:
    fixed_width, fixed_height = random.uniform(0.1, 0.5), random.uniform(0.1, 0.5)

for _ in range(num_papers):
    x, y = random_point_in_circle(circle_diameter / 2)
    if uniform_size:
        width, height = fixed_width, fixed_height
    else:
        width, height = random.uniform(0.1, 0.5), random.uniform(0.1, 0.5)
    create_paper(x, y, paper_thickness / 2, width, height, paper_thickness, collectioname)
