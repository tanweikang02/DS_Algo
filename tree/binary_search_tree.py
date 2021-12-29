# Binary Search Tree implemented using the concept of nodes


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.is_leaf = self.left == None and self.right == None


class BinarySearchTree:
    def __init__(self):
        self.root_node = None
        self.size = 0

    def insert(self, data):
        node = Node(data)
        if self.root_node == None:
            self.root_node = node
        else:
            parent = None
            current = self.root_node
            direction = None

            while True:
                if current == None:
                    if direction == "left":
                        parent.left = node
                    else:
                        parent.right = node
                    self.size += 1
                    return

                elif data >= current.data:
                    parent = current
                    current = current.right
                    direction = "right"

                elif data <= current.data:
                    parent = current
                    current = current.left
                    direction = "left"

    def inorder_traverse(self, root_node):
        current = root_node
        if current == None:
            return
        self.inorder_traverse(current.left)
        print(current.data)
        self.inorder_traverse(current.right)

    def preorder_traverse(self, root_node):
        current = root_node
        if current == None:
            return
        print(current.data)
        self.preorder_traverse(current.left)
        self.preorder_traverse(current.right)

    def postorder_traverse(self, root_node):
        current = root_node
        if current == None:
            return
        self.postorder_traverse(current.left)
        self.postorder_traverse(current.right)
        print(current.data)


bst = BinarySearchTree()
bst.insert(15)
bst.insert(12)
bst.insert(42)
bst.insert(8)
bst.insert(26)
bst.insert(13)
bst.insert(14)

bst.postorder_traverse(bst.root_node)
