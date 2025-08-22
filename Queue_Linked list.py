class Node:
    def __init__(self, car_no):
        self.car_no = car_no
        self.next = None

class CarParking:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    # Car enters parking (Enqueue)
    def car_entry(self, car_no):
        new_car = Node(car_no)
        if self.rear is None: # Parking empty
            self.front = self.rear = new_car
        else:
            self.rear.next = new_car
            self.rear = new_car
        print(f"Car {car_no} entered parking.")

    # Car leaves parking (Dequeue)
    def car_exit(self):
        if self.is_empty():
            print("Parking is empty. No cars to exit.")
            return
        car_no = self.front.car_no
        self.front = self.front.next
        if self.front is None: # Parking became empty
            self.rear = None
        print(f"Car {car_no} exited parking.")

    # Show first car to leave next
    def next_exit(self):
        if self.is_empty():
            print("Parking is empty.")
        else:
            print(f"Next car to exit: {self.front.car_no}")

    # Display all parked cars
    def display_parking(self):
        if self.is_empty():
            print("Parking is empty.")
            return
        temp = self.front
        print("Cars in parking:")
        while temp:
            print(temp.car_no, end=" -> ")
            temp = temp.next
        print("None")

# Menu driven
parking = CarParking()
while True:
    print("\n--- Car Parking System ---")
    print("1. Car Entry")
    print("2. Car Exit")
    print("3. Show Next Car to Exit")
    print("4. Display All Cars in Parking")
    print("5. Exit")
    
    ch = input("Enter choice: ")

    if ch == '1':
        car_no = input("Enter Car Number: ")
        parking.car_entry(car_no)
    elif ch == '2':
        parking.car_exit()
    elif ch == '3':
        parking.next_exit()
    elif ch == '4':
        parking.display_parking()
    elif ch == '5':
        print("Exiting system...")
        break
    else:
        print("Invalid choice.")
