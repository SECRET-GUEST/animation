import bpy
import os

# Path to the folder where you want to save the GLB files
output_folder = "your path"

# Counter for naming the files
file_counter = 1

def select_armature_and_children(armature):
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature

    for obj in armature.children:
        obj.select_set(True)

for armature in bpy.data.objects:
    if armature.type == 'ARMATURE':
        select_armature_and_children(armature)
        
        # Output file name (dancer1, dancer2, etc.)
        output_file = os.path.join(output_folder, f"dancer{file_counter}.glb")
        file_counter += 1

        # Export as GLB with settings optimized for Three.js
        bpy.ops.export_scene.gltf(
            filepath=output_file, 
            export_format='GLB',
            use_selection=True, 
            export_apply=True,
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            # Additional settings for Three.js optimization
            export_image_format='AUTO',
            export_texture_dir='',  # You can specify a directory for textures if needed
            export_extras=True,     # Export additional data required for Three.js
            export_yup=True         # Export with Y axis as vertical axis
        )

print("Export completed.")

