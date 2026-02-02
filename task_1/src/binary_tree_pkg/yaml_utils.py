import yaml
from .node import Node

def build_tree_from_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        return _dict_to_node(data)
    except Exception as e:
        print(f"Error reading YAML: {e}")
        return None

def _dict_to_node(data):
    if not data or 'value' not in data:
        return None
    
    node = Node(data['value'])
    
    # 1. Check for General Tree format ("children" list)
    if 'children' in data and isinstance(data['children'], list):
        for child_data in data['children']:
            child_node = _dict_to_node(child_data)
            if child_node:
                node.add_child(child_node)
                
    # 2. Backward Compatibility: Check for Binary Tree format ("left/right")
    elif 'left' in data or 'right' in data:
        if 'left' in data:
            node.left = _dict_to_node(data['left'])
        if 'right' in data:
            node.right = _dict_to_node(data['right'])
            
    return node

def write_tree_to_yaml(root, file_path):
    """Writes the tree structure to YAML."""
    data = _node_to_dict(root)
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

def _node_to_dict(node):
    if not node:
        return None
    
    data = {'value': node.value}
    
    # Convert children list to YAML format
    if node.children:
        data['children'] = [_node_to_dict(child) for child in node.children]
        
    return data