class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        data = self.front.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print("Deleted:", data)

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.front:
                break

        print()


cq = CircularQueue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        cq.enqueue(data)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.peek()

    elif choice == 4:
        cq.display()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")