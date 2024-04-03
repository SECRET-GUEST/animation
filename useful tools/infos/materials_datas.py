# This script will get all datas from images textures with their size and their URL
# It's useful to optimise size from your textures.

import bpy
import os

# Path where the text file will be saved
output_file_path = 'YOUR PATH HERE /materials_info.txt'

def get_image_size(image):
    """ Returns the size of the image in megabytes. """
    try:
        file_path = bpy.path.abspath(image.filepath_raw)
        return os.path.getsize(file_path) / (1024 * 1024)  # Converts bytes to megabytes
    except:
        return 0

def main():
    total_size_mb = 0
    materials_info = []

    # Iterate through all materials in the project
    for mat in bpy.data.materials:
        if mat.node_tree:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE':
                    image = node.image
                    if image:
                        size_mb = get_image_size(image)
                        total_size_mb += size_mb
                        materials_info.append({"name": mat.name, "path": image.filepath, "size": size_mb})

    # Sorting the materials by texture size in descending order
    materials_info.sort(key=lambda x: x["size"], reverse=True)

    with open(output_file_path, 'w') as file:
        for info in materials_info:
            file.write("-----------------------------------\n")
            file.write(f"Material: {info['name']}\n")
            file.write(f"Texture: {info['path']}\n")
            file.write(f"Size: {info['size']:.2f} MB\n")

        file.write(f"\nTotal texture size: {total_size_mb:.2f} MB\n")

# Execute the main function
main()
