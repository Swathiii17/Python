stack = []
MAX = 5 # Maximum size of stack

def push():
    if len(stack) == MAX:
        print("Stack is Full!")
    else:
        item = input("Enter item to push: ")
        stack.append(item)
        print(f"{item} pushed into the stack.")

def pop():
    if not stack:
        print("Stack is Empty!")
    else:
        item = stack.pop()
        print(f"{item} popped from the stack.")

def peek():
    if not stack:
        print("Stack is Empty!")
    else:
        print("Top of stack:", stack[-1])

def display():
    print("Stack (top to bottom):", stack[::-1])

# Menu
while True:
    print("\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
