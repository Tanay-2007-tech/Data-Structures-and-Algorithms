class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            data = self.front.data

            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next

            self.size -= 1
            print("Deleted:", data)

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Peek:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


q1 = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        item = int(input("Enter value: "))
        q1.enqueue(item)

    elif choice == 2:
        q1.dequeue()

    elif choice == 3:
        q1.peek()

    elif choice == 4:
        q1.display()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")