# print all the left nodes of a tree
# print all the right nodes of a tree
# print all the root nodes of a tree

# https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f




class BinarySearchNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent # help for removing operation

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinarySearchNode(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                return self.insert_node(data, node.left_node)
            node.left_node = BinarySearchNode(data, node)
        else:
            if node.right_node:
                return self.insert_node(data, node.right_node)
            node.right_node = BinarySearchNode(data, node)
                


    def get_min(self):
        if self.root:
            return self.calculate_min(self.root)


    def calculate_min(self, node):
        if node.left_node:
            return self.calculate_min(node.left_node)
        return node.data


    def get_max(self):
        if self.root:
            return self.calculate_max(self.root)
    
    def calculate_max(self, node):
        if node.right_node:
            return self.calculate_max(node.right_node)
        return node.data


    def traverse(self):
        if self.root:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)
        if node.right_node:
            return self.traverse_in_order(node.right_node)


    def remove(self, data):
        if self.root:
            return self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return 

        if data < node.data:
            return self.remove_node(data, node.left_node)
        elif data > node.data:
            return self.remove_node(data, node.right_node)

        else:
            # we found the node that need to remove
            # there could be three option

            # removing a leaf node
            if node.left_node is None and node.right_node is None: 
                print("Removing a leaf node...", node.data)
                parent = node.parent
                if parent and parent.left_node == node:
                    parent.left_node = None
                elif parent and parent.right_node == node:
                    parent.right_node = None

                elif parent is None: # root node dont have a parent
                    self.root = None

                del node

            # when there is single right child
            elif node.left_node is None and node.right_node:
                print("Removing a node with a single right child: ", node.data)

                parent = node.parent

                if parent and parent.left_node == node:
                    parent.left_node = node.right_node

                elif parent and parent.right_node == node:
                    parent.right_node = node.right_node

                elif parent is None:
                    self.root = node.right_node

                # node.right_node.parent = parent 
                node.right_node.parent = node.parent 

                del node

            # when there is single left child
            elif node.right_node is None and node.left_node:
                print("Removing a node with a single left child: ", node.data)

                parent = node.parent

                if parent and parent.right_node == node:
                    parent.right_node = node.left_node

                elif parent and parent.left_node == node:
                    parent.left_node = node.left_node

                elif parent is None:
                    self.root = node.left_node

                # node.right_node.parent = node.parent 
                node.left_node.parent = parent 

                del node
            # removing node with two children
            else:
                print("Removing a node with two children: ", node.data)

                predecessor = self.get_predecessor(node.left_node)


                # swap the node with the predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)


    def get_predecessor(self, node): 
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node
    

class BSTCompare:
    def compare(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2

        # we have to check the value in the group
        if node1.data is not node2.data:
            return False

        # check all the right and left subtree
        return self.compare(node1.left_node, node2.left_node) and self.compare(node1.right_node, node2.right_node)

bst = BinarySearchTree()

bst.insert(1)
bst.insert(2)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(4)
bst.insert(3)


bst2 = BinarySearchTree()

bst2.insert(1)
bst2.insert(2)
bst2.insert(3)
bst2.insert(4)
bst2.insert(5)
bst2.insert(6)


compareBST = BSTCompare()

binary_tree = BinaryTree()

