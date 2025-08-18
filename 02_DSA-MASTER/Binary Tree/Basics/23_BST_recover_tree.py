# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if self.prev and self.prev.val > root.val:
            if self.first is None:
                self.first = self.prev
            self.second = root

        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root):
        self.inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


# Helper function to print tree in inorder
def inorder_print(root):
    if root is None:
        return
    inorder_print(root.left)
    print(root.val, end=" ")
    inorder_print(root.right)


# ✅ Construct a BST with two nodes swapped
# Original BST:
#     3
#    / \
#   1   4
#      /
#     2
#
# Swapped version (2 and 3 are swapped):
#     2
#    / \
#   1   4
#      /
#     3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)  # 3 and 2 are swapped

# ✅ Before recovery
print("Inorder traversal before recovery:")
inorder_print(root)

# ✅ Recover tree
solution = Solution()
solution.recoverTree(root)

# ✅ After recovery
print("\nInorder traversal after recovery:")
inorder_print(root)

# ✅ Show detected swapped nodes
if solution.first and solution.second:
    print(f"\nSwapped nodes were: {solution.first.val} and {solution.second.val}")
else:
    print("\nNo swapped nodes were detected.")
