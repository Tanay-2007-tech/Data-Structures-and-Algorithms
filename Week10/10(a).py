
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    # Get height
    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    # Get balance factor
    def getBalance(self, root):
        if root is None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    # Right rotation
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))

        return x

    # Left rotation
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))

        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        return y

    # Insert
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            print("Duplicate value not allowed")
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        # LL Case
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)

        # RR Case
        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)

        # LR Case
        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL Case
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Search
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    # Preorder
    def preOrder(self, root):
        if root:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    # Postorder
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")

    # Find minimum
    def findMin(self, root):
        if root is None:
            return None

        while root.left:
            root = root.left

        return root.data

    # Find maximum
    def findMax(self, root):
        if root is None:
            return None

        while root.right:
            root = root.right

        return root.data

    # Count nodes
    def countNodes(self, root):
        if root is None:
            return 0

        return (1 + self.countNodes(root.left)
                  + self.countNodes(root.right))

    # Height
    def height(self, root):
        if root is None:
            return -1

        return max(self.height(root.left),
                   self.height(root.right)) + 1

    # Level order helper
    def printLevel(self, root, level):
        if root is None:
            return

        if level == 0:
            print(root.data, end=" ")
        else:
            self.printLevel(root.left, level - 1)
            self.printLevel(root.right, level - 1)

    # Level order
    def levelOrder(self, root):
        h = self.height(root)

        for level in range(h + 1):
            self.printLevel(root, level)

    # Delete
    def delete(self, root, key):

        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # Case 1 and Case 2
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 3
            temp = root.right

            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        # Update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        # LL Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # LR Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RR Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # RL Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


# Main program
tree = AVL()
root = None

while True:

    print("\n\n****** AVL TREE ******")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Find Minimum")
    print("7. Find Maximum")
    print("8. Count Nodes")
    print("9. Height")
    print("10. Level Order Traversal")
    print("11. Delete")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        root = tree.insert(root, data)
        print("Insertion completed")

    elif choice == 2:
        key = int(input("Enter value to search: "))

        if tree.search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        print("Inorder:", end=" ")
        tree.inOrder(root)
        print()

    elif choice == 4:
        print("Preorder:", end=" ")
        tree.preOrder(root)
        print()

    elif choice == 5:
        print("Postorder:", end=" ")
        tree.postOrder(root)
        print()

    elif choice == 6:
        print("Minimum:", tree.findMin(root))

    elif choice == 7:
        print("Maximum:", tree.findMax(root))

    elif choice == 8:
        print("Total nodes:", tree.countNodes(root))

    elif choice == 9:
        print("Height:", tree.height(root))

    elif choice == 10:
        print("Level order:", end=" ")
        tree.levelOrder(root)
        print()

    elif choice == 11:
        key = int(input("Enter value to delete: "))

        if tree.search(root, key):
            root = tree.delete(root, key)
            print("Deletion completed")
        else:
            print("Element not found")

    elif choice == 12:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
