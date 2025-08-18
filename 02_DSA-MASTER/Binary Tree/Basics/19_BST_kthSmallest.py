# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.count = 0
        self.result = -1

    def kthSmallest(self, root, k):
        self.helper(root, k)
        return self.result

    def helper(self, root, k):
        if root is None:
            return

        # Traverse left
        self.helper(root.left, k)

        # Visit current node
        self.count += 1
        if self.count == k:
            self.result = root.val
            return

        # Traverse right
        self.helper(root.right, k)



root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

solution = Solution()
print(solution.kthSmallest(root, 1))