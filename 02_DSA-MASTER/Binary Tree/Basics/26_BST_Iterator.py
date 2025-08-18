# 173. Binary Search Tree Iterator

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        top = self.stack.pop()
        if top.right:
            self._leftmost_inorder(top.right)
        return top.val

    def hasNext(self):
        return len(self.stack) > 0

# Example usage:
# Construct a simple BST:
#      7
#     / \
#    3   15
#        / \
#       9  20

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    obj = BSTIterator(root)
    while obj.hasNext():
        print(obj.next(), end=" ")  # Output: 3, 7, 9, 15, 20