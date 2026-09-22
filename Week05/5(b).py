
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter the no of elements: "))
        for i in range(n):
            x = int(input("Enter the value: "))
            new = Node(x)

            if self.head is None:
                self.head = new
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new
                new.prev = temp

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end="<->")
            current = current.next
        print("None")

    def insert_begindl(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_enddl(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begindl(data)
            return

        if self.head is None:
            print("Invalid index")
            return

        new = Node(data)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                print("Invalid index")
                return

        new.next = temp.next
        new.prev = temp

        if temp.next:
            temp.next.prev = new

        temp.next = new

    def delete_atbegindl(self):
        if self.head is None:
            print("Delete operation can't be performed")
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_atenddl(self):
        if self.head is None:
            print("Delete operation can't be performed")
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    def delete_at_index(self, index):
        if index < 0:
            print("Invalid index")
            return

        if self.head is None:
            print("Deletion operation can't be performed")
            return

        if index == 0:
            self.delete_atbegindl()
            return

        temp = self.head

        for i in range(index):
            temp = temp.next
            if temp is None:
                print("Invalid index")
                return

        if temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


dl = DoublyLinkedList()

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
        dl.create()

    elif choice == 2:
        dl.display()

    elif choice == 3:
        data = int(input("Enter the value: "))
        dl.insert_begindl(data)

    elif choice == 4:
        data = int(input("Enter the value: "))
        dl.insert_enddl(data)

    elif choice == 5:
        index = int(input("Enter the index: "))
        data = int(input("Enter the value: "))
        dl.insert_at_index(index, data)

    elif choice == 6:
        dl.delete_atbegindl()

    elif choice == 7:
        dl.delete_atenddl()

    elif choice == 8:
        index = int(input("Enter the index: "))
        dl.delete_at_index(index)

    elif choice == 9:
        break

    else:
        print("Invalid choice")

