import bpy

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

# Call the function to create the teardrop shape
create_teardrop('Teardrop', 3.5, 4, 0.1)
