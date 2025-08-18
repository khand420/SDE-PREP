class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ✅ 1. Height of a Tree
# Definition: The height is the number of edges on the longest path from the root to a leaf node. (Some definitions use the number of nodes instead of edges — here, we’ll use edges.)

def height(root):
    if not root:
        return -1  # height of empty tree is -1 (edge count)
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def sum_nodes(root):
    if not root:
        return 0
    return root.val + sum_nodes(root.left) + sum_nodes(root.right)



# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5

# Run the functions
print("Height of tree:", height(root))        # Output: 2 (edges: 1→2→4 or 1→2→5)
print("Total nodes:", count_nodes(root))      # Output: 5
print("Sum of all nodes:", sum_nodes(root))   # Output: 1+2+3+4+5 = 15
