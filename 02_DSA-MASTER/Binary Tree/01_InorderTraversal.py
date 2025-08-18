# Step 1: Define TreeNode
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 2: Define Recursive Inorder
def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

# Step 3: Define Iterative Inorder
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result

# Step 4: Build test tree
# Example Tree:
#         1
#          \
#           2
#          /
#         3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Step 5: Run tests
print("Recursive Inorder:", inorder_recursive(root))  # Output: [1, 3, 2]
print("Iterative Inorder:", inorder_iterative(root))  # Output: [1, 3, 2]
