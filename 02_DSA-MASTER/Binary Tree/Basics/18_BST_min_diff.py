# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None
        self.min_diff = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return self.min_diff
        
        # In-order traversal: Left
        self.minDiffInBST(root.left)
        
        # Visit current node
        if self.prev is not None:
            self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val

        # In-order traversal: Right
        self.minDiffInBST(root.right)

        return self.min_diff
    


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
print(solution.minDiffInBST(root))