class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity # fixed size array
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, car):
        if self.is_full():
            print("Queue is full. Cannot add more cars.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = car
        self.size += 1
        print(f"Car '{car}' added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No car to remove.")
            return None
        car = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Car '{car}' removed from the queue.")
        return car

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Current Queue of Cars:")
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(f"- {self.queue[index]}")

# Program starts here (no main function)
parking_queue = Queue(capacity=5)

while True:
    print("\n--- Car Parking System ---")
    print("1. Park a Car (Enqueue)")
    print("2. Remove a Car (Dequeue)")
    print("3. Show All Cars")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        car_num = input("Enter Car Number: ")
        parking_queue.enqueue(car_num)
    elif choice == "2":
        parking_queue.dequeue()
    elif choice == "3":
        parking_queue.display_queue()
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Please try again.")
