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
                
#                                 load all your 3D files from a batch faster          |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#         https://github.com/SECRET-GUEST/animation/tree/blender/IMPORT%20EXPORT/IMPORT/3D%20FILES/batchloader
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
import time,bpy,os

#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Path to the folder containing 3D files
folder_path = '/PUT/YOUR/PATH/HERE'   # Replace for your folder path
include_subfolders = False            # Include subfolders in the folder selected ? 
import_delay = 0                      # If big amount of files, you want to delay between each import to avoid blender crash

# If both true, it will generate objects in one collection including collections for all objects
include_in_a_single_collection = True
include_in_object_collection = True

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
     
     
def create_or_get_collection(collection_name, parent_collection=None):
    if collection_name in bpy.data.collections:
        return bpy.data.collections[collection_name]
    else:
        new_collection = bpy.data.collections.new(collection_name)
        if parent_collection:
            parent_collection.children.link(new_collection)
        else:
            bpy.context.scene.collection.children.link(new_collection)
        return new_collection

def import_to_collection(filepath):
    # Determine the collection names
    main_collection_name = 'imported' if include_in_a_single_collection else None
    object_collection_name = os.path.splitext(os.path.basename(filepath))[0] if include_in_object_collection else None

    # Create or get the main collection
    main_collection = create_or_get_collection(main_collection_name) if main_collection_name else None

    # Create or get the object specific collection
    object_collection = create_or_get_collection(object_collection_name, main_collection) if object_collection_name else main_collection

    # Import the file
    import_file(filepath)

    # Add imported objects to the specified collection
    if object_collection:
        for obj in bpy.context.selected_objects:
            # Ensure object isn't already linked to another collection
            for coll in obj.users_collection:
                coll.objects.unlink(obj)
            object_collection.objects.link(obj)

def import_file(filepath):
    try:
        extension = os.path.splitext(filepath)[1].lower()
        # Import logic for different file formats (same as previously provided)
    except Exception as e:
        print(f"Error importing file {filepath}: {e}")
    time.sleep(import_delay)  # Delay after each import



def import_file(filepath):
    try:
        extension = os.path.splitext(filepath)[1].lower()
        if extension == '.obj':
            bpy.ops.import_scene.obj(filepath=filepath)
        elif extension == '.fbx':
            bpy.ops.import_scene.fbx(filepath=filepath)
        elif extension == '.stl':
            bpy.ops.import_mesh.stl(filepath=filepath)
        elif extension == '.dae':
            bpy.ops.wm.collada_import(filepath=filepath)
        elif extension == '.ply':
            bpy.ops.import_mesh.ply(filepath=filepath)
        elif extension == '.3ds':
            bpy.ops.import_scene.autodesk_3ds(filepath=filepath)
        elif extension == '.gltf' or extension == '.glb':
            bpy.ops.import_scene.gltf(filepath=filepath)
        elif extension == '.x3d':
            bpy.ops.import_scene.x3d(filepath=filepath)
        elif extension == '.abc':
            bpy.ops.wm.alembic_import(filepath=filepath)
        elif extension == '.bvh':
            bpy.ops.import_anim.bvh(filepath=filepath)
        elif extension == '.svg':
            bpy.ops.import_curve.svg(filepath=filepath)
        elif extension == '.lwo':
            bpy.ops.import_scene.lwo(filepath=filepath)
        elif extension == '.vrml':
            bpy.ops.import_scene.vrml2(filepath=filepath)
        elif extension == '.dxf':
            bpy.ops.import_scene.dxf(filepath=filepath)
        # Add other file formats here if needed
        else:
            print(f"Unsupported or unrecognized file extension: {extension}")
    except Exception as e:
        print(f"Error importing file {filepath}: {e}")
    time.sleep(import_delay)  # delay after importing

def process_folder(path):
    for entry in os.scandir(path):
        if entry.is_file():
            import_to_collection(entry.path)
        elif entry.is_dir() and include_subfolders:
            process_folder(entry.path)

process_folder(folder_path)
