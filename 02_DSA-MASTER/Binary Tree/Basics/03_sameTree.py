# same tree 
# is tree identical 
# 100. Same Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.data != q.data:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)




# Tree 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Tree 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(isSameTree(root1, root2))  # Output: True
