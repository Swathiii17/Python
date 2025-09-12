class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)

    def _preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')

# Example usage
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

print("Inorder traversal:")
tree.inorder() # Output: 1 3 4 6 7 8 10 13 14
print("\nPreorder traversal:")
tree.preorder() # Output: 8 3 1 6 4 7 10 14 13
print("\nPostorder traversal:")
tree.postorder() # Output: 1 4 7 6 3 13 14 10 8
