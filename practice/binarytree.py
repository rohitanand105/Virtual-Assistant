class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from collections import deque

def insert_level_order(root, value):
    """
    Inserts a value into the binary tree in level order.
    """
    new_node = TreeNode(value)
    
    if root is None:  # If tree is empty, new node becomes the root
        return new_node
    
    queue = deque([root])  # Use a queue to traverse the tree in level order
    while queue:
        current = queue.popleft()
        
        if not current.left:  # If left child is empty, insert the new node here
            current.left = new_node
            break
        else:
            queue.append(current.left)
        
        if not current.right:  # If right child is empty, insert the new node here
            current.right = new_node
            break
        else:
            queue.append(current.right)
    
    return root

def in_order(node):

    if node is None:
        return
    
    if node:
        
        in_order(node.left)
        print(node.value , " ")
        in_order(node.right)


root = None

values = [10,20,30,40,50,60,70]

for value in values:
    root = insert_level_order(root, value)

    print("in order traversal of the binary tree")
    in_order(root)

    
