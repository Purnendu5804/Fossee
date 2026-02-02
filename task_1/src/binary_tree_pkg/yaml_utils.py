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
    
    # Recursively build left and right children
    if 'left' in data:
        node.left = _dict_to_node(data['left'])
    if 'right' in data:
        node.right = _dict_to_node(data['right'])
        
    return node

def write_tree_to_yaml(root, file_path):
    data = _node_to_dict(root)
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

def _node_to_dict(node):
    if not node:
        return None
    
    data = {'value': node.value}
    if node.left:
        data['left'] = _node_to_dict(node.left)
    if node.right:
        data['right'] = _node_to_dict(node.right)
    return data