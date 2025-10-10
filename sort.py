def bubble_sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

def insertion_sort(marks):
    for i in range(1, len(marks)):
        key = marks[i]
        j = i - 1
        while j >= 0 and marks[j] > key:
            marks[j + 1] = marks[j]
            j -= 1
        marks[j + 1] = key

def selection_sort(marks):
    n = len(marks)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if marks[j] < marks[min_index]:
                min_index = j
        marks[i], marks[min_index] = marks[min_index], marks[i]

marks = [75, 60, 85, 50, 90, 70]
print("Original marks:", marks)

bubble_sorted = marks.copy()
bubble_sort(bubble_sorted)
print("Marks after Bubble Sort:", bubble_sorted)

insertion_sorted = marks.copy()
insertion_sort(insertion_sorted)
print("Marks after Insertion Sort:", insertion_sorted)

selection_sorted = marks.copy()
selection_sort(selection_sorted)
print("Marks after Selection Sort:", selection_sorted)
