# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def helper(self, nums, st, end):
        if st > end:
            return None

        mid = st + (end - st) // 2
        root = TreeNode(nums[mid])

        root.left = self.helper(nums, st, mid - 1)
        root.right = self.helper(nums, mid + 1, end)

        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.helper(nums, 0, len(nums) - 1)



def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

nums = [-10, -3, 0, 5, 9]
sol = Solution()
bst_root = sol.sortedArrayToBST(nums)

print("Inorder Traversal of BST:")
inorderTraversal(bst_root)
