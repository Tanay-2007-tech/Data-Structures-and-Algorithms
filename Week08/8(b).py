class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')

        self.root.left.left = Node('D')
        self.root.left.right = Node('E')

        self.root.right.right = Node('F')

    def preOrder(self, node):
        if node is None:
            return

        print(node.data, end=",")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end=",")
        self.inOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=",")

    def Levelorder(self):
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


tree = BinaryTree()

tree.create_tree()

print("PreOrder Traversal:")
tree.preOrder(tree.root)
print()
print("InOrder Traversal:")
tree.inOrder(tree.root)
print()
print("PostOrder Traversal:")
tree.postOrder(tree.root)
print()
print("LevelOrder Traversal:")
tree.Levelorder()


