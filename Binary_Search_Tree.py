class Node:
    def __init__(self, name, entry_time, purpose):
        self.name = name
        self.entry_time = entry_time
        self.purpose = purpose
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

   
    def insert(self, root, name, entry_time, purpose):
        if root is None:
            return Node(name, entry_time, purpose)

        if name < root.name:
            root.left = self.insert(root.left, name, entry_time, purpose)
        else:
            root.right = self.insert(root.right, name, entry_time, purpose)

        return root

 
    def search(self, root, name):
        if root is None or root.name == name:
            return root
        if name < root.name:
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

 
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

   
    def delete(self, root, name):
        if root is None:
            return root

        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
           
            if root.left is None and root.right is None:
                return None

         
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

         
            temp = self.minValueNode(root.right)
            root.name, root.entry_time, root.purpose = temp.name, temp.entry_time, temp.purpose
            root.right = self.delete(root.right, temp.name)

        return root

   
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.name} | {root.entry_time} | {root.purpose}")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(f"{root.name} | {root.entry_time} | {root.purpose}")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"{root.name} | {root.entry_time} | {root.purpose}")

   
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)



if __name__ == "__main__":
    bst = BST()
    root = None

    while True:
        print("\n--- Visitor Log Book (BST) ---")
        print("1. Insert Log Entry")
        print("2. Delete Log Entry")
        print("3. Search Log Entry")
        print("4. Traverse Log Entries (Inorder)")
        print("5. Traverse Log Entries (Preorder)")
        print("6. Traverse Log Entries (Postorder)")
        print("7. Count Total Entries")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Visitor Name: ")
            entry_time = input("Enter Entry Time: ")
            purpose = input("Enter Purpose: ")
            root = bst.insert(root, name, entry_time, purpose)
            print("Log entry inserted successfully.")

        elif choice == "2":
            name = input("Enter Visitor Name to delete: ")
            root = bst.delete(root, name)
            print("Log entry deleted (if found).")

        elif choice == "3":
            name = input("Enter Visitor Name to search: ")
            result = bst.search(root, name)
            if result:
                print(f"Found: {result.name} | {result.entry_time} | {result.purpose}")
            else:
                print("Log entry not found.")

        elif choice == "4":
            print("\nInorder Traversal (Sorted by Name):")
            bst.inorder(root)

        elif choice == "5":
            print("\nPreorder Traversal:")
            bst.preorder(root)

        elif choice == "6":
            print("\nPostorder Traversal:")
            bst.postorder(root)

        elif choice == "7":
            total = bst.count_nodes(root)
            print(f"Total entries in log book: {total}")

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
