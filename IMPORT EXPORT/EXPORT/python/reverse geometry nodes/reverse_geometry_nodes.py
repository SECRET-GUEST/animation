import bpy
import os

# Specify the path where the script will be saved
save_path = r"your \path\here"

def format_value(value):
    if isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif hasattr(value, "to_tuple"):  # For vectors and similar objects
        return str(value.to_tuple())
    elif isinstance(value, (list, tuple)):
        return str(tuple(value))
    return "None"

def get_node_details(node):
    details = {
        'name': node.name.replace(' ', '_').replace('.', '_'),  # Replace spaces and dots with underscores
        'type': node.bl_idname,
        'location': (node.location[0], node.location[1]),
        'inputs': {input.name: (input.default_value if hasattr(input, 'default_value') and not input.is_linked else None) for input in node.inputs if hasattr(input, 'default_value')},
        'outputs': {output.name: output.is_linked for output in node.outputs}
    }
    return details

def get_node_connections(node_tree):
    connections = []
    for node in node_tree.nodes:
        for output in node.outputs:
            if output.is_linked:
                for link in output.links:
                    to_node = link.to_node
                    connections.append((node.name.replace(' ', '_').replace('.', '_'), output.name, to_node.name.replace(' ', '_').replace('.', '_'), link.to_socket.name))
    return connections

def generate_node_tree_script(node_tree, file_path):
    nodes = [get_node_details(node) for node in node_tree.nodes]
    connections = get_node_connections(node_tree)
    
    with open(file_path, 'w') as f:
        f.write("import bpy\n\n")
        f.write("def create_geometry_node_tree(obj):\n")
        f.write("    node_tree = bpy.data.node_groups.new('Color_edges', 'GeometryNodeTree')\n")
        f.write("    node_group_input = node_tree.nodes.new('NodeGroupInput')\n")
        f.write("    node_group_output = node_tree.nodes.new('NodeGroupOutput')\n")
        f.write("    node_group_input.location = (-200, 0)\n")
        f.write("    node_group_output.location = (200, 0)\n\n")
        
        # Write nodes
        for node in nodes:
            f.write(f"    {node['name']} = node_tree.nodes.new('{node['type']}')\n")
            f.write(f"    {node['name']}.location = {node['location']}\n")
            for input_name, value in node['inputs'].items():
                if value is not None:
                    formatted_value = format_value(value)
                    if formatted_value != "None":
                        f.write(f"    if '{input_name}' in {node['name']}.inputs:\n")
                        f.write(f"        {node['name']}.inputs['{input_name}'].default_value = {formatted_value}\n")
            if node['type'] == 'GeometryNodeSetMaterial' and node['inputs'].get('Material') is not None:
                f.write(f"    {node['name']}.inputs['Material'].default_value = bpy.data.materials['{node['inputs']['Material'].name}']\n")
            f.write("\n")
        
        # Write connections
        for from_node, from_socket, to_node, to_socket in connections:
            if 'NodeGroupInput' in from_node or 'NodeGroupOutput' in to_node:
                # Create dummy nodes for visualization
                if 'NodeGroupInput' in from_node:
                    dummy_node_name = f"dummy_output_{from_socket}"
                    dummy_node = "node_tree.nodes.new('NodeReroute')"
                    dummy_location = f"({nodes[0]['location'][0] - 100}, {nodes[0]['location'][1]})"
                    f.write(f"    {dummy_node_name} = {dummy_node}\n")
                    f.write(f"    {dummy_node_name}.location = {dummy_location}\n")
                    f.write(f"    node_tree.links.new({from_node}.outputs['{from_socket}'], {dummy_node_name}.inputs[0])\n")
                if 'NodeGroupOutput' in to_node:
                    dummy_node_name = f"dummy_input_{to_socket}"
                    dummy_node = "node_tree.nodes.new('NodeReroute')"
                    dummy_location = f"({nodes[-1]['location'][0] + 100}, {nodes[-1]['location'][1]})"
                    f.write(f"    {dummy_node_name} = {dummy_node}\n")
                    f.write(f"    {dummy_node_name}.location = {dummy_location}\n")
                    f.write(f"    node_tree.links.new({dummy_node_name}.outputs[0], {to_node}.inputs['{to_socket}'])\n")
            else:
                f.write(f"    if '{from_socket}' in {from_node}.outputs and '{to_socket}' in {to_node}.inputs:\n")
                f.write(f"        node_tree.links.new({from_node}.outputs['{from_socket}'], {to_node}.inputs['{to_socket}'])\n")
        
        f.write("\n    # Apply node tree to object\n")
        f.write("    if not hasattr(obj, 'modifiers'):\n")
        f.write("        raise AttributeError('Selected object does not support modifiers')\n")
        f.write("    modifier = obj.modifiers.new(name='GeometryNodes', type='NODES')\n")
        f.write("    modifier.node_group = node_tree\n")
        f.write("\ncreate_geometry_node_tree(bpy.context.object)\n")

# Select the object with the Geometry Nodes modifier
obj = bpy.context.object

# Ensure the object has a Geometry Nodes modifier
geo_nodes_modifier = None
for modifier in obj.modifiers:
    if modifier.type == 'NODES':
        geo_nodes_modifier = modifier
        break

if geo_nodes_modifier:
    node_tree = geo_nodes_modifier.node_group
    # Generate the filename based on the node tree name
    file_name = f"GEO_{node_tree.name.replace(' ', '_').replace('.', '_')}.py"
    file_path = os.path.join(save_path, file_name)
    generate_node_tree_script(node_tree, file_path)
    print(f"Script saved to {file_path}")
else:
    print("No Geometry Nodes modifier found on the selected object.")
