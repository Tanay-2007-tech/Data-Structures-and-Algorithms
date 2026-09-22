#using array

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Popped:", self.stack.pop())
            self.top -= 1

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top:", self.stack[self.top])

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()


size = int(input("Enter stack size: "))
s = Stack(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the value: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")

