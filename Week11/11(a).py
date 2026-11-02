class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print("Element found")
        else:
            print("Element not found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable(10)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter element: "))
        ht.insert(key)

    elif choice == 2:
        key = int(input("Enter element to search: "))
        ht.search(key)

    elif choice == 3:
        ht.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")