# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def inorder(self, root, result):
        if root is None:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

    def merge(self, arr1, arr2):
        merged = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged

    def sortedArrayToBST(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        node.left = self.sortedArrayToBST(arr, start, mid - 1)
        node.right = self.sortedArrayToBST(arr, mid + 1, end)
        return node

    def mergeTwoBSTs(self, root1, root2):
        arr1 = []
        arr2 = []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        merged_arr = self.merge(arr1, arr2)
        return self.sortedArrayToBST(merged_arr, 0, len(merged_arr) - 1)



# BST 1:     2
#           / \
#          1   3

# BST 2:     7
#           / \
#          6   8

t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)

t2 = TreeNode(7)
t2.left = TreeNode(6)
t2.right = TreeNode(8)

sol = Solution()
new_root = sol.mergeTwoBSTs(t1, t2)

# Print inorder of the merged tree (should be [1, 2, 3, 6, 7, 8])
def inorderPrint(node):
    if node:
        inorderPrint(node.left)
        print(node.val, end=" ")
        inorderPrint(node.right)

inorderPrint(new_root)  # Output: 1 2 3 6 7 8
