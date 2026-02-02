class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

def add_node_by_path(root, path, value):  
    #Adds a node at the specific 'L' (Left) / 'R' (Right) path.
   
    if not root:
        return Node(value)
    
    current = root
    # Navigate to the parent of the new node
    for char in path[:-1]:
        if char.upper() == 'L':
            if not current.left:
                current.left = Node(None) 
            current = current.left
        elif char.upper() == 'R':
            if not current.right:
                current.right = Node(None)
            current = current.right
    

    direction = path[-1].upper()
    if direction == 'L':
        current.left = Node(value)
    elif direction == 'R':
        current.right = Node(value)

def delete_node(root, value):

    if not root:
        return None
    
    if root.value == value:
        return None                           # Removing this link drops the subtree
    
    root.left = delete_node(root.left, value)
    root.right = delete_node(root.right, value)
    return root

def print_tree(root, prefix="", is_left=None):
    
    if not root:
        return

   
    if prefix == "":
        print(f"Root:{root.value}")
    else:
        print(f"{prefix}{root.value}")

    

    new_prefix = "L---" if is_left else "R---"
    

    if root.left:
        print_tree(root.left, "L---", is_left=True)
    elif root.right:         # If right exists but left doesn't, we usually print a placeholder?
         print("L---None")

    if root.right:
        print_tree(root.right, "R---", is_left=False)
    elif root.left:                                   # If left exists but right doesn't
         print("R---None")