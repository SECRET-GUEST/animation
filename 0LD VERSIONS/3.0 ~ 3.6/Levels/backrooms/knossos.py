import bpy
import random

class LabyrinthParameters:
    def __init__(self):
        self.level_size = (100, 100)
        self.wall_collections = ["1", "2", "3"]
        self.object_collections = ["c", "p", "b"]
        self.passage_size = 2
        self.random_passage_size = False
        self.room_size = 5
        self.random_room_size = False
        self.light_level = 'semi_lit'

params = LabyrinthParameters()

def create_floor_and_ceiling(params):
    bpy.ops.mesh.primitive_plane_add(size=params.level_size[0], enter_editmode=False, align='WORLD', location=(params.level_size[0]/2, params.level_size[1]/2, 0))
    bpy.ops.mesh.primitive_plane_add(size=params.level_size[1], enter_editmode=False, align='WORLD', location=(params.level_size[0]/2, params.level_size[1]/2, 3))

def create_lights(params):
    light_material = bpy.data.materials.new(name="lumieres_plafond")
    light_material.use_nodes = True
    light_material.node_tree.nodes.clear()
    output = light_material.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    emission = light_material.node_tree.nodes.new(type='ShaderNodeEmission')
    light_material.node_tree.links.new(emission.outputs['Emission'], output.inputs['Surface'])
    emission.inputs['Strength'].default_value = 50
    return light_material

def instance_object_from_collection(collection):
    for obj in collection.objects:
        instance = obj.copy()
        instance.data = obj.data.copy()
        instance.animation_data_clear()
        return instance
    return None

def create_maze(params):
    bpy.ops.object.select_all(action='DESELECT')
    create_floor_and_ceiling(params)
    light_material = create_lights(params)

    grid_size = 0.5
    max_distance = 3
    prev_x, prev_y = -max_distance * 2, -max_distance * 2

    for x in range(int(params.level_size[0] / grid_size)):
        for y in range(int(params.level_size[1] / grid_size)):
            if random.random() > 0.95 and (x == 0 or abs(x - prev_x) >= max_distance * 2) and (y == 0 or abs(y - prev_y) >= max_distance * 2):
                bpy.ops.mesh.primitive_plane_add(size=grid_size, enter_editmode=False, align='WORLD', location=(x * grid_size, y * grid_size, 3))
                obj = bpy.context.active_object
                obj.data.materials.append(light_material)
                prev_x, prev_y = x, y

            if random.random() > 0.9:
                wall_collection_name = random.choice(params.wall_collections)
                wall_collection = bpy.data.collections.get(wall_collection_name)
                if wall_collection:
                    wall_instance = instance_object_from_collection(wall_collection)
                    if wall_instance:
                        wall_instance.location = (x * grid_size + grid_size/2, y * grid_size + grid_size/2, 1.5)
                        bpy.context.collection.objects.link(wall_instance)

            if random.random() > 0.95:
                object_collection_name = random.choice(params.object_collections)
                object_collection = bpy.data.collections.get(object_collection_name)
                if object_collection:
                    object_instance = instance_object_from_collection(object_collection)
                    if object_instance:
                        object_instance.location = (x * grid_size + grid_size / 2, y * grid_size + grid_size / 2, 0)
                        bpy.context.collection.objects.link(object_instance)



def main():
    create_maze(params)

if __name__ == "__main__":
    main()
