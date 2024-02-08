import bpy

# Iterate over all images loaded in Blender
for image in bpy.data.images:
    # Check if the image is "baked"
    if "Bake" in image.name:
        # Remove the image
        bpy.data.images.remove(image)

print("Bake removal completed.")
