from binary_tree_pkg import Node, add_node_by_path, print_tree, build_tree_from_yaml
import os

if __name__ == "__main__":
    # 1. Manual Tree Construction
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print("Manual Tree:")
    print_tree(root)


    root = Node(10)
    print("\nInitial tree:")
    print_tree(root)

    print("\nAdding nodes:")
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RL", 12)
    add_node_by_path(root, "RR", 18)

    print("\nTree after additions:")
    print_tree(root)

    # 3. YAML Test
    yaml_file = "test.yaml" 
    if os.path.exists(yaml_file):
        print(f"\nBuilding tree from '{yaml_file}':")
        yaml_tree_root = build_tree_from_yaml(yaml_file)
        
        if yaml_tree_root:
            print("\nTree built from YAML:")
            print_tree(yaml_tree_root)
    else:
        print(f"\nWarning: {yaml_file} not found. Run this script from the 'tests' folder.")