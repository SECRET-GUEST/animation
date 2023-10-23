#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                            This python script allows Blender to 
                
#                            randomly generate objects duplicated from selected              |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
#                     objects on 1 selected object surface like a  character or whatever
#                                  |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                   |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#          
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
               
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|

#You don't have to import with pip, just paste the code in blender     
          
import bpy,bmesh,random, bisect, math
from mathutils import Vector
from mathutils.bvhtree import BVHTree

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

#Function to create a new collection with a given name and optionally a parent collection
def create_collection(name, parent_collection=None):

    #Create a new collection 
    new_collection = bpy.data.collections.new(name)

    #If a parent collection is provided, link the new collection as a child of the parent
    if parent_collection:
        parent_collection.children.link(new_collection)

    #Otherwise, link the new collection as a child of the scene's top-level collection
    else:
        bpy.context.scene.collection.children.link(new_collection)


    #Then return the newly created collection
    return new_collection




#Function to merge all objects in a given collection into a new object in a target collection
def merge_objects_in_collection(target_collection, collection_name, new_object_name):


    collection = bpy.data.collections[collection_name]     #Get the collection of objects to merge
    mesh = bpy.data.meshes.new(new_object_name)            #Create a new mesh for the merged object
    obj = bpy.data.objects.new(new_object_name, mesh)      # Create a new object using the new mesh

    target_collection.objects.link(obj)                    #Link the new object to the target collection

    bm = bmesh.new()                                       #Create a new BMesh to merge the meshes of all objects in the collection

    #Iterate through all objects in the collection
    for obj_to_merge in collection.objects:
        if obj_to_merge.type == 'MESH':                    #If the object is a mesh, merge its geometry into the BMesh

            mesh_to_merge = obj_to_merge.data
            transform = obj_to_merge.matrix_world
            bmesh.ops.transform(bm, verts=bm.verts, matrix=transform)
            bm.from_mesh(mesh_to_merge)
                                                           #Then convert the merged BMesh back to a mesh and free the BMesh
    bm.to_mesh(mesh)
    bm.free()


    return obj





#Function to create a new mechanical part by copying an existing part, optionally from a collection
def create_mech_part(collection, part_name, location, rotation):

    #Check if the part exists in a collection
    if part_name in bpy.data.collections:

        #Merge all objects in the part's collection into a new object in the given collection
        collection_object = merge_objects_in_collection(collection, part_name, f"{part_name}_object")

        #Use the new merged object as a template for the new part
        part_template = collection_object


    else:
        #Otherwise, use the existing object as a template for the new part
        part_template = bpy.data.objects[part_name]
    

    part = part_template.copy()                 #Create a new copy of the part template object
    part.data = part_template.data.copy()       #Copy the data block of the part template

    part.location = location                    #Set the part's location and rotation
    part.rotation_euler = rotation

    collection.objects.link(part)               #Then add the new part to the given collection
    

    return part






#Function to generate a BVHTree from a character object
def get_character_bvh_tree(character):
    
    depsgraph = bpy.context.evaluated_depsgraph_get()       #Get the evaluated dependency graph and create a new BMesh from the character object

    bm = bmesh.new()
    bm.from_object(character, depsgraph)                    #Transform the BMesh by the character's world matrix
    bm.transform(character.matrix_world)                    #Convert the BMesh to a BVHTree and return it


    return BVHTree.FromBMesh(bm)






#Function to generate a random point on the surface of a character object
def get_surface_point(character, bvh_tree):

    #Get the evaluated dependency graph and create a new mesh from the character object
    depsgraph = bpy.context.evaluated_depsgraph_get()
    mesh = character.evaluated_get(depsgraph).to_mesh()

    #Create a list of cumulative areas for each face in the mesh
    areas_cumulative = [0]

    for face in mesh.polygons:
        areas_cumulative.append(areas_cumulative[-1] + face.area)

    #Choose a random face index based on the cumulative areas
    random_area = random.uniform(0, areas_cumulative[-1])
    random_face_index = bisect.bisect(areas_cumulative, random_area) - 1
    random_face = mesh.polygons[random_face_index]

    #Choose a random point on the face
    verts = [mesh.vertices[v].co for v in random_face.vertices]
    u, v = random.random(), random.random()

    if u + v > 1:
        u, v = 1 - u, 1 - v

    point_on_face = (1 - u - v) * verts[0] + u * verts[1] + v * verts[2]

    #Convert the point to world coordinates
    surface_point = character.matrix_world @ point_on_face

    #Don't forget to clear the mesh
    character.to_mesh_clear()


    return surface_point



#Function to generate a specified number of mechanical parts on the surface of a character object
def generate_mech_parts(character, part_names, num_parts, use_symmetry):

    #Generate a BVHTree from the character object
    character_bvh_tree = get_character_bvh_tree(character)
    mech_parts = []
    
    #Create a new collection for the generated parts
    new_parts_collection = create_collection("Generated_Mech_Parts")

    #Generate the specified number of parts
    for _ in range(num_parts // 2 if use_symmetry else num_parts):

        location = get_surface_point(character, character_bvh_tree)                         #Get a random surface point on the character
        rotation = Vector([random.uniform(0, math.pi) for _ in range(3)])                   #Generate a random rotation for the part
        part_name = random.choice(part_names)                                               #Choose random part name
        part = create_mech_part(new_parts_collection, part_name, location, rotation)        #Create a new mechanical part using the part name and surface point

        mech_parts.append(part)

        # f using symmetry, create a mirrored part on the opposite side of the character
        if use_symmetry:
            mirrored_location = location * Vector([-1, 1, 1])
            mirrored_rotation = Vector([rotation[0], -rotation[1], -rotation[2]])
            mirrored_part = create_mech_part(new_parts_collection, part_name, mirrored_location, mirrored_rotation)
            mech_parts.append(mirrored_part)


    return mech_parts






#Parameters :
character = bpy.data.objects['character']   #Choose the object where will be generated/ duplicated the objects  
part_names = ('1', '2', '3')                #Choose objects you want to generate (you can use collections name here)
num_parts = 5                               #Choose number max you can generate
use_symmetry = True                         #Choose if you want to use symmetry

#Then generate parts on the object
mech_parts = generate_mech_parts(character, part_names, num_parts, use_symmetry)
