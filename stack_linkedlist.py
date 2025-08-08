class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"{value} pushed into the stack.")

    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
        else:
            popped = self.top.data
            self.top = self.top.next
            print(f"{popped} popped from the stack.")

    def peek(self):
        if self.top is None:
            print("Stack is Empty!")
        else:
            print("Top of stack:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is Empty!")
        else:
            temp = self.top
            print("Stack (top to bottom):")
            while temp:
                print(temp.data, end=" --> ")
                temp = temp.next
            print("NULL")

# Menu
stack = Stack()
while True:
    print("\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter item to push: ")
        stack.push(val)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
