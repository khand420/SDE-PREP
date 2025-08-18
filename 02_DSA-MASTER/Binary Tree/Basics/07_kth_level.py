from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def kthLevel(root, k):
    if root is None:
        return
    if k == 1:
        print(root.data, end=" ")
        return
    
    kthLevel(root.left, k-1)
    kthLevel(root.right, k-1)

    

    return 

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

kthLevel(root, 3)



    #    1
    #  /   \
    # 2     3
    #  \   / \
    #   4 5   6
