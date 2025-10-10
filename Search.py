# Program: Implementation of Linear Search and Binary Search

# Function for Linear Search
def linear_search(roll_list, key):
    for i in range(len(roll_list)):
        if roll_list[i] == key:
            return i
    return -1

# Function for Binary Search
def binary_search(roll_list, key):
    low = 0
    high = len(roll_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if roll_list[mid] == key:
            return mid
        elif roll_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main Program
roll_numbers = [101, 105, 109, 112, 118, 120, 125]
print("Registered roll numbers:", roll_numbers)

key = int(input("Enter roll number to search: "))

# Linear Search
pos1 = linear_search(roll_numbers, key)
if pos1 != -1:
    print(f"Linear Search: Roll number {key} found at position {pos1 + 1}")
else:
    print(f"Linear Search: Roll number {key} not found.")

# Binary Search (List should be sorted)
sorted_rolls = sorted(roll_numbers)
pos2 = binary_search(sorted_rolls, key)
if pos2 != -1:
    print(f"Binary Search: Roll number {key} found at position {pos2 + 1}")
else:
    print(f"Binary Search: Roll number {key} not found.")
