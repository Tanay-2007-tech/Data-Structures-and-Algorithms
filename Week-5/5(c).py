
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter the no of elements: "))

        for i in range(n):
            x = int(input("Enter the value: "))
            new = Node(x)

            if self.head is None:
                self.head = new
                new.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new
                new.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end="->")
            temp = temp.next

            if temp == self.head:
                break

        print("(HEAD)")

    def insert_begincll(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new.next = self.head
            temp.next = new
            self.head = new

    def insert_endcll(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new
            new.next = self.head

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begincll(data)
            return

        if self.head is None:
            print("Invalid index")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid index")
                return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_at_begincll(self):
        if self.head is None:
            print("Delete operation can't be performed")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next

    def delete_at_endcll(self):
        if self.head is None:
            print("Delete operation can't be performed")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head

    def delete_at_index(self, index):
        if index < 0:
            print("Invalid index")
            return

        if self.head is None:
            print("Deletion operation can't be performed")
            return

        if index == 0:
            self.delete_at_begincll()
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid index")
                return

        if temp.next == self.head:
            print("Invalid index")
            return

        temp.next = temp.next.next


cll = CircularLinkedList()

while True:
    print("\n1. Create")
    print("2. Display")
    print("3. Insert at Beginning")
    print("4. Insert at End")
    print("5. Insert at Index")
    print("6. Delete at Beginning")
    print("7. Delete at End")
    print("8. Delete at Index")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.display()

    elif choice == 3:
        data = int(input("Enter the value: "))
        cll.insert_begincll(data)

    elif choice == 4:
        data = int(input("Enter the value: "))
        cll.insert_endcll(data)

    elif choice == 5:
        index = int(input("Enter the index: "))
        data = int(input("Enter the value: "))
        cll.insert_at_index(index, data)

    elif choice == 6:
        cll.delete_at_begincll()

    elif choice == 7:
        cll.delete_at_endcll()

    elif choice == 8:
        index = int(input("Enter the index: "))
        cll.delete_at_index(index)

    elif choice == 9:
        break

    else:
        print("Invalid choice")

