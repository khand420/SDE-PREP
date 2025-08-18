# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def helper(self, root, minNode, maxNode):
        if root is None:
            return True

        if minNode is not None and root.val <= minNode.val:
            return False

        if maxNode is not None and root.val >= maxNode.val:
            return False

        return self.helper(root.left, minNode, root) and self.helper(root.right, root, maxNode)

    def isValidBST(self, root):
        return self.helper(root, None, None)



# Valid BST
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sol = Solution()
print(sol.isValidBST(root))  # Output: True
