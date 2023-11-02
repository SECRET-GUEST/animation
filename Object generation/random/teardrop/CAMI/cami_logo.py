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
                
#        |                                This script allows Blender to 
                
#                                   generate a logo of CAMI (Common Artificial               |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#                 Modular Intelligence) based on gathering of several Artificial intelligences
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
import math

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

def create_teardrop(name, width, height, thickness):
    # Create a new curve object
    curve_data = bpy.data.curves.new(name, type='CURVE')
    curve_data.dimensions = '3D'
    curve_data.fill_mode = 'FULL'
    curve_data.extrude = thickness / 2
    
    # Create a new object and link the curve data
    curve_obj = bpy.data.objects.new(name, curve_data)
    bpy.context.scene.collection.objects.link(curve_obj)
    
    # Create the teardrop shape using Bezier curves
    polyline = curve_data.splines.new('BEZIER')
    polyline.bezier_points.add(2)  # Add two bezier points
    
    # Set the control points and handles for the bezier curve
    # to create a symmetrical teardrop shape
    polyline.bezier_points[0].co = (0, -height/2, 0)
    polyline.bezier_points[0].handle_right = (width/2, -height/2, 0)
    polyline.bezier_points[0].handle_left = (-width/2, -height/2, 0)
    
    polyline.use_cyclic_u = True  # Close the curve
    
    # Set the curve object to be the active object
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    # Add a Solidify modifier to the curve object with complex mode and 0.2m thickness
    solidify_modifier = curve_obj.modifiers.new(name="Solidify", type='SOLIDIFY')
    solidify_modifier.thickness = 0.2
    solidify_modifier.solidify_mode = 'NON_MANIFOLD'  # Set to complex mode
    

    return curve_obj

# generate 3 teardrops
teardrop1 = create_teardrop('Teardrop1', 3.5, 4, 0.1)
teardrop2 = create_teardrop('Teardrop2', 3.5, 4, 0.1)
teardrop3 = create_teardrop('Teardrop3', 3.5, 4, 0.1)



# Move up each teardrops
for teardrop in [teardrop1, teardrop2, teardrop3]:
    teardrop.location.y += 2 

# generate empty
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
empty = bpy.context.active_object

# Path tracing of the empty to turn around
for teardrop in [teardrop1, teardrop2, teardrop3]:
    constraint = teardrop.constraints.new(type='TRACK_TO')
    constraint.target = empty
    constraint.track_axis = 'TRACK_NEGATIVE_Y'
    constraint.up_axis = 'UP_Z'


# Unselect all
bpy.ops.object.select_all(action='DESELECT')

# Select and turn t teardrop2
teardrop2.select_set(True)
bpy.context.view_layer.objects.active = teardrop2
bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z', center_override=empty.location)

# Unselect teardrop2
teardrop2.select_set(False)

# Select and turn teardrop3
teardrop3.select_set(True)
bpy.context.view_layer.objects.active = teardrop3
bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z', center_override=empty.location)



# Place all in collections
if "teardrops" not in bpy.data.collections:
    teardrops = bpy.data.collections.new("teardrops")
    bpy.context.scene.collection.children.link(teardrops)
else:
    teardrops = bpy.data.collections["teardrops"]

# Unlink from default collection and link to teardrops collection
default_collection = bpy.context.scene.collection
for obj in [teardrop1, teardrop2, teardrop3]:
    default_collection.objects.unlink(obj)
    teardrops.objects.link(obj)

# Convert each teardrop to mesh
bpy.ops.object.select_all(action='DESELECT')
for teardrop in [teardrop1, teardrop2, teardrop3]:
    teardrop.select_set(True)
    bpy.context.view_layer.objects.active = teardrop
    bpy.ops.object.convert(target='MESH')
    teardrop.select_set(False)

# Delete the empty object
bpy.ops.object.select_all(action='DESELECT')
empty.select_set(True)
bpy.ops.object.delete()


# Remove constraints linking the 3 item to the center of the world
for teardrop in [teardrop1, teardrop2, teardrop3]:
    constraint_to_remove = [c for c in teardrop.constraints if c.type == 'TRACK_TO']
    for constraint in constraint_to_remove:
        teardrop.constraints.remove(constraint)
