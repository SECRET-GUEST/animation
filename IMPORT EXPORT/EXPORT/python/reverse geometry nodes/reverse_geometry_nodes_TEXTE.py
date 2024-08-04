import bpy
import os
import tempfile

def get_node_details(node):
    details = f"Node: {node.name} ({node.bl_idname})\n"
    for input in node.inputs:
        if input.is_linked:
            details += f"  Input {input.name}: Linked to {input.links[0].from_node.name} ({input.links[0].from_socket.name})\n"
        else:
            if hasattr(input, 'default_value'):
                details += f"  Input {input.name}: {input.default_value}\n"
    for output in node.outputs:
        if output.is_linked:
            linked_nodes = [f"{link.to_node.name} ({link.to_socket.name})" for link in output.links]
            details += f"  Output {output.name}: Linked to {', '.join(linked_nodes)}\n"
        else:
            details += f"  Output {output.name}: Not Linked\n"
    return details

def get_node_connections(node_tree):
    connections = []
    for node in node_tree.nodes:
        node_name = node.name
        for output in node.outputs:
            if output.is_linked:
                for link in output.links:
                    to_node = link.to_node
                    connections.append((node_name, to_node.name))
    return connections

def generate_detailed_info(node_tree):
    details = []
    
    for node in node_tree.nodes:
        details.append(get_node_details(node))
    
    return details

def generate_connections_info(connections):
    info = ["\nConnections:\n"]
    for from_node, to_node in connections:
        info.append(f"{from_node} ----> {to_node}")
    return info

def get_material_names(node_tree):
    materials = []
    for node in node_tree.nodes:
        if node.bl_idname == 'GeometryNodeSetMaterial':
            material_name = node.inputs['Material'].default_value.name if node.inputs['Material'].default_value else 'None'
            materials.append(f"Node: {node.name} uses material: {material_name}")
    return materials

# Sélectionne l'objet avec le modificateur Geometry Nodes
obj = bpy.context.object

# Assure-toi que l'objet a un modificateur Geometry Nodes
geo_nodes_modifier = None
for modifier in obj.modifiers:
    if modifier.type == 'NODES':
        geo_nodes_modifier = modifier
        break

if geo_nodes_modifier:
    node_tree = geo_nodes_modifier.node_group
    connections = get_node_connections(node_tree)
    
    node_details = generate_detailed_info(node_tree)
    connections_info = generate_connections_info(connections)
    material_names = get_material_names(node_tree)
    
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:
        temp_file.write(f"Node Tree: {node_tree.name}\n\n")
        for detail in node_details:
            temp_file.write(detail + "\n")
        for line in connections_info:
            temp_file.write(line + "\n")
        temp_file.write("\nMaterial Names:\n")
        for material in material_names:
            temp_file.write(material + "\n")
        temp_file_path = temp_file.name
    
    os.system(f"notepad {temp_file_path}")
else:
    print("Aucun modificateur Geometry Nodes trouvé sur l'objet sélectionné.")
