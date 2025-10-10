class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, root):
        if not root:
            return 0
        return root.height

    def balance_factor(self, root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, id, name):
        if not root:
            return Node(id, name)
        if id < root.id:
            root.left = self.insert(root.left, id, name)
        elif id > root.id:
            root.right = self.insert(root.right, id, name)
        else:
            return root # duplicate not allowed

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        # Balance cases
        if balance > 1 and id < root.left.id:
            return self.right_rotate(root)
        if balance < -1 and id > root.right.id:
            return self.left_rotate(root)
        if balance > 1 and id > root.left.id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and id < root.right.id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.id, "-", root.name)
            self.inorder(root.right)

    def search(self, root, id):
        if not root:
            return None
        if root.id == id:
            return root
        elif id < root.id:
            return self.search(root.left, id)
        else:
            return self.search(root.right, id)

    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


# ---------------- MAIN PROGRAM (with input inside) ----------------

avl = AVLTree()
root = None

# Predefined Student Enrollments
students = [
    (105, "Kavzz"),
    (101, "Arun"),
    (110, "Priya"),
    (108, "Ravi"),
    (102, "Latha")
]

# Insert students into AVL Tree
for id, name in students:
    root = avl.insert(root, id, name)

print("📘 Student Enrollment Records (Inorder):")
avl.inorder(root)

# Search example
print("\n🔍 Searching for Enrollment ID 108:")
s = avl.search(root, 108)
if s:
    print("Found:", s.id, "-", s.name)
else:
    print("Not found!")

# Count total records
print("\n📊 Total Enrollments:", avl.count(root))
