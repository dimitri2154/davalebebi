class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printLeafNodes(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        else:
            printLeafNodes(root.left)
            printLeafNodes(root.right)

def countEdges(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 0
    else:
        return 1 + countEdges(root.left) + countEdges(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf nodes:")
printLeafNodes(root)
print("\nNumber of edges:", countEdges(root))