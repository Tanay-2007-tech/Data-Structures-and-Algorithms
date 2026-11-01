
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    # Find height
    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    # Calculate balance factor
    def getBalance(self, root):
        if root is None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    # Right rotation (LL case)
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

    # Left rotation (RR case)
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
            return root

        # Update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Calculate balance factor
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

    # Inorder traversal
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    # Preorder traversal
    def preOrder(self, root):
        if root:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    # Postorder traversal
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")

    # Find minimum node
    def findMin(self, root):
        if root is None:
            return None

        while root.left:
            root = root.left

        return root.data


# Main program
tree = AVL()
root = None

values = [10, 20, 30, 40, 50, 25]

for i in values:
    root = tree.insert(root, i)

print("Inorder Traversal:")
tree.inOrder(root)

print("\nPreorder Traversal:")
tree.preOrder(root)

print("\nPostorder Traversal:")
tree.postOrder(root)

key = 30

if tree.search(root, key):
    print("\nElement Found")
else:
    print("\nElement Not Found")
