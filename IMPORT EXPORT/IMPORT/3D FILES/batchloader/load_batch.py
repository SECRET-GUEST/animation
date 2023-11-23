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
#               
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
import os

#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Path to the folder containing 3D files
folder_path = 'C:/path/to/the/folder'


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
     

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

# Iterate through the folder and import each file
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        import_file(file_path)
