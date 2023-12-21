import bpy

# Renames mesh data based on the collection name containing the object
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.users_collection:
        collection_name = obj.users_collection[0].name
        obj.data.name = collection_name + "_" + obj.name
