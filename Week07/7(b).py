class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return

        data = self.queue[self.front]
        self.front += 1
        print("Deleted:", data)

        if self.front > self.rear:
            self.front = -1
            self.rear = -1

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


size = int(input("Enter size of queue: "))
q = Queue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        q.enqueue(data)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")