from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def topView(root):
    if not root:
        return []

    # Queue of elements (node, horizontal_distance)
    q = deque()
    q.append((root, 0))
    
    # Dictionary to store the topmost node at each horizontal distance
    top_nodes = {}

    min_hd = max_hd = 0

    while q:
        node, hd = q.popleft()

        # If horizontal distance is not already present, set it
        if hd not in top_nodes:
            top_nodes[hd] = node.data

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    # Extracting the top view nodes from min_hd to max_hd
    result = []
    for hd in range(min_hd, max_hd + 1):
        result.append(top_nodes[hd])

    return result

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(topView(root))



    #    1
    #  /   \
    # 2     3
    #  \   / \
    #   4 5   6
