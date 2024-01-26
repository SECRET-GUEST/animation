import bpy

# Rename the mesh object datas
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.users_collection:
        # Use first collection name then object name
        collection_name = obj.users_collection[0].name
        obj.data.name = collection_name + "_" + obj.name