# WAP to find the Height/depth/rank of a Binary Tree - SOLVED
# traverse binary tree: Pre-order, In-order, Post-order - SOLVED
# convert traversing (pre-post, post-pre, in-pre..) in any one of three orders
# check if the tree is the balanced binary tree or not
# check if the tree is the complete binary tree or not
# check if the tree is symmetric or not (i.e., left and right subtree mirror each other.)
# check if the two trees are identical or not

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    
    return max(left_height, right_height) + 1

def is_symmetric(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.value == right.value) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)
def is_mirror(left, right):

    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return (left.value == right.value) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

# in-order : left -> node(root) -> right 
def inorder_traversal(node):
    if node is None:
        return []
    left_traversal = inorder_traversal(node.left)
    current_value = [node.value]
    right_traversal = inorder_traversal(node.right)
    
    return left_traversal + current_value + right_traversal

# pre-order : node(root) -> left -> right 
def preorder_traversal(node):
    if node is None:
        return []
    current_node = [node.value]
    left_traversal = preorder_traversal(node.left)
    right_traversal = preorder_traversal(node.right)

    return current_node + left_traversal + right_traversal 

# post-order : left -> right -> node(root)
def postorder_traversal(node):
    if node is None:
        return []
    
    left_traversal = postorder_traversal(node.left)
    right_traversal = postorder_traversal(node.right)
    current_node = [node.value]

    return left_traversal + right_traversal + current_node

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# tree_height = height(root)
# print("Height of the binary tree:", tree_height)

print("is Symmetric Binary Tree: ", is_symmetric(root))

# print("In-order traversal: ", inorder_traversal(root))

# print("Pre-order traversal: ", preorder_traversal(root))

# print("Post-order traversal: ", postorder_traversal(root))
