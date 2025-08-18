# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestBSTSubtree(self, root):
        self.max_size = 0
        
        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))  # isBST, size, min, max
            
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)
            
            # Check BST validity
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_size = left_size + right_size + 1
                self.max_size = max(self.max_size, current_size)
                return (True, current_size, min(node.val, left_min), max(node.val, right_max))
            else:
                return (False, 0, 0, 0)
        
        dfs(root)
        return self.max_size




# Binary Tree:
#         10
#        /  \
#       5    15
#      / \     \
#     1   8     7

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.largestBSTSubtree(root))  # Output: 3 (subtree rooted at 5)
