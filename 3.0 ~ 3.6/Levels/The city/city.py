import bpy
import bmesh
import random
from math import radians
from mathutils import Vector

# Fonction pour créer une porte
def create_door(bm, building_width, building_depth):
    door_height = 3
    door_width = 1.5

    verts = bmesh.ops.create_cube(bm, size=1)["verts"]
    bmesh.ops.scale(bm, vec=(door_width / 2, building_depth / 2, door_height / 2), verts=verts)
    bmesh.ops.translate(bm, verts=verts, vec=(0, 0, door_height / 2))

# Fonction pour créer une fenêtre
def create_window(bm, building_width, building_depth, floor, num_floors, window_width, window_height):
    window_offset_x = random.uniform(-(building_width / 2) + window_width / 2, (building_width / 2) - window_width / 2)
    window_offset_y = random.uniform(-(building_depth / 2) + window_height / 2, (building_depth / 2) - window_height / 2)
    window_offset_z = floor * (window_height + 1) + window_height / 2 + 1

    if floor < num_floors - 1:
        verts = bmesh.ops.create_cube(bm, size=1)["verts"]
        bmesh.ops.scale(bm, vec=(window_width / 2, building_depth / 2, window_height / 2), verts=verts)
        bmesh.ops.translate(bm, verts=verts, vec=(window_offset_x, window_offset_y, window_offset_z))

# Fonction pour créer un building
def create_building(location, building_width, building_depth, num_floors, add_windows, add_door):
    mesh_data = bpy.data.meshes.new("building")
    building_obj = bpy.data.objects.new("building", mesh_data)
    building_obj.location = location

    bm = bmesh.new()
    base_verts = bmesh.ops.create_cube(bm, size=1)["verts"]

    bmesh.ops.scale(bm, vec=(building_width / 2, building_depth / 2, num_floors / 2), verts=base_verts)

    if add_door:
        create_door(bm, building_width, building_depth)

    if add_windows:
        window_width = 1
        window_height = 2
        for floor in range(num_floors - 1):
            create_window(bm, building_width, building_depth, floor, num_floors, window_width, window_height)

    bm.to_mesh(mesh_data)
    bm.free()

    # Ajoute l'objet à la scène
    bpy.context.collection.objects.link(building_obj)

# Paramètres
num_buildings = 58
min_floors = 1
max_floors = 10
min_building_width = 4
max_building_width = 8
min_building_depth = 4
max_building_depth = 8
add_windows = True
add_door = True
perimeter = 20

# Génère les bâtiments
for i in range(num_buildings):
    building_width = random.uniform(min_building_width, max_building_width)
    building_depth = random.uniform(min_building_depth, max_building_depth)
    num_floors = random.randint(min_floors, max_floors)
    location_x = random.uniform(-perimeter / 2, perimeter / 2)
    location_y = random.uniform(-perimeter / 2, perimeter / 2)
    location = Vector((location_x, location_y, 0))

    create_building(location, building_width, building_depth, num_floors, add_windows, add_door)
