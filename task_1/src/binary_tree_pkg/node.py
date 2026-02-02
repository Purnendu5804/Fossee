class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # Bonus: Can hold any number of children now

    def add_child(self, node):
        """Bonus: Helper to add a child to a general tree."""
        self.children.append(node)

    # --- Backward Compatibility for Binary Tree Task ---
    @property
    def left(self):
        """Virtual property to make 'left' point to children[0]"""
        return self.children[0] if len(self.children) > 0 else None

    @left.setter
    def left(self, node):
        """Allows root.left = Node(x) to work by manipulating the list"""
        if not node: return # Ignore setting None
        if len(self.children) == 0:
            self.children.append(node)
        else:
            self.children[0] = node

    @property
    def right(self):
        """Virtual property to make 'right' point to children[1]"""
        return self.children[1] if len(self.children) > 1 else None

    @right.setter
    def right(self, node):
        """Allows root.right = Node(x) to work"""
        if not node: return
        # Ensure we have a slot for 'left' first (even if None/placeholder)
        while len(self.children) < 1:
            self.children.append(Node(None))
        
        if len(self.children) == 1:
            self.children.append(node)
        else:
            self.children[1] = node
            
    def __repr__(self):
        return f"Node({self.value})"

# --- Updated Helper Functions ---

def add_node_by_path(root, path, value):

    if not root:
        return Node(value)
    
    current = root

    for char in path[:-1]:
        if char.upper() == 'L':
            if not current.left: current.left = Node(None)
            current = current.left
        elif char.upper() == 'R':
            if not current.right: current.right = Node(None)
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
        return None
    
   
    new_children = []
    for child in root.children:
        cleaned_child = delete_node(child, value)
        if cleaned_child:
            new_children.append(cleaned_child)
    
    root.children = new_children
    return root

def print_tree(root, prefix="", is_last=True):
   
    if not root:
        return

    print(prefix + ("└── " if is_last else "├── ") + str(root.value))
    
    prefix += "    " if is_last else "│   "
    
    count = len(root.children)
    for i, child in enumerate(root.children):
        is_last_child = (i == count - 1)
        print_tree(child, prefix, is_last_child)