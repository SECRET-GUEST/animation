import bpy
import os
import tempfile

# Settings
target_node_name = "Cyclic Animator"  # Leave empty to process all nodes or specify the name of the node

# Function to get node details and their connections
def get_node_details(node, depth=0):
    indent = "  " * depth  # Indentation for nested groups
    details = f"{indent}Node: {node.name} ({node.bl_idname})\n"
    
    # List inputs
    for input in node.inputs:
        if input.is_linked:
            details += f"{indent}  Input {input.name}: Linked to {input.links[0].from_node.name} ({input.links[0].from_socket.name})\n"
        elif hasattr(input, 'default_value'):
            details += f"{indent}  Input {input.name}: {input.default_value}\n"
    
    # List outputs
    for output in node.outputs:
        if output.is_linked:
            linked_nodes = [f"{link.to_node.name} ({link.to_socket.name})" for link in output.links]
            details += f"{indent}  Output {output.name}: Linked to {', '.join(linked_nodes)}\n"
        else:
            details += f"{indent}  Output {output.name}: Not Linked\n"
    
    # Process sub-groups if any
    if hasattr(node, "node_tree") and node.node_tree is not None:
        details += f"\n{indent}  --- Sub-node group details for {node.name} ---\n"
        for sub_node in node.node_tree.nodes:
            details += get_node_details(sub_node, depth + 1)  # Recursively process sub-nodes
    
    return details

# Function to generate detailed information, including node connections
def generate_detailed_info(node_tree, target_node_name=None):
    details = []
    if target_node_name:  # Manual mode
        node = node_tree.nodes.get(target_node_name)
        if node:
            details.append(get_node_details(node))
    else:  # Automatic mode (all nodes)
        for node in node_tree.nodes:
            details.append(get_node_details(node))
    return details

# Function to get material names
def get_material_names(node_tree, target_node_name=None):
    materials = []
    if target_node_name:
        node = node_tree.nodes.get(target_node_name)
        if node and node.bl_idname == 'GeometryNodeSetMaterial':
            material_name = node.inputs['Material'].default_value.name if node.inputs['Material'].default_value else 'None'
            materials.append(f"Node: {node.name} uses material: {material_name}")
    else:
        for node in node_tree.nodes:
            if node.bl_idname == 'GeometryNodeSetMaterial':
                material_name = node.inputs['Material'].default_value.name if node.inputs['Material'].default_value else 'None'
                materials.append(f"Node: {node.name} uses material: {material_name}")
    return materials

# Main script logic
def main():
    node_tree = bpy.data.node_groups.get("Drawing thunder")  # Replace with your node group name
    if node_tree:
        # Retrieve node details
        node_details = generate_detailed_info(node_tree, target_node_name)
        material_names = get_material_names(node_tree, target_node_name)

        # Check if there are any nodes in the node tree
        if not node_tree.nodes:
            print(f"Node tree '{node_tree.name}' contains no nodes.")
            return

        # Write the results to a temporary text file
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:
            temp_file.write(f"Node Tree: {node_tree.name}\n\n")
            for detail in node_details:
                temp_file.write(detail + "\n")
            if material_names:
                temp_file.write("\nMaterial Names:\n")
                for material in material_names:
                    temp_file.write(material + "\n")
            temp_file_path = temp_file.name
        
        # Open the file in the default text editor
        os.system(f"notepad {temp_file_path}")
    else:
        print("No node tree found.")

# Run the script
main()
