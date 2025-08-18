class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(p, q):
    if p is None and q is None:
        return True

    return p.data == q.data and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSubTree(root, subRoot):
    if subRoot is None:
        return True  # An empty tree is always a subtree
    if root is None:
        return False  # Non-empty subtree can't be found in empty tree

    if isSameTree(root, subRoot):
        return True

    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)




# Main Tree
root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(2)

# Subtree
subRoot = Node(4)
subRoot.left = Node(1)
subRoot.right = Node(2)

print(isSubTree(root, subRoot))  # Output: True
