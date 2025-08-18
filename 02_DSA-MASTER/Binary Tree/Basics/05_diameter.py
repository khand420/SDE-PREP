# 1. diameter through 
#     len = lh = rh
# 2. right diaemeter
# 3. left diameter


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 0

    def height(self, node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)

        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.ans



obj = TreeNode(1)
obj.left = TreeNode(2)
obj.right = TreeNode(3)
obj.right.left = TreeNode(4)
obj.right.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(obj))