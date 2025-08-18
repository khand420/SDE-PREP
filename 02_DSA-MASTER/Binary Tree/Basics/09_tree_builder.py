# Definition for a binary tree node.

# 105. Construct Binary Tree from Preorder and Inorder Traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
#         self.preIndex = 0

#         def helper(left, right):
#             if left > right:
#                 return None

#             root_val = preorder[self.preIndex]
#             self.preIndex += 1
#             root = TreeNode(root_val)

#             idx = inorder_index_map[root_val]
#             root.left = helper(left, idx - 1)
#             root.right = helper(idx + 1, right)
#             return root

#         return helper(0, len(inorder) - 1)



class Solution(object):
    def search(self, inorder, left, right, val):
        for i in range(left, right):
            if inorder[i] == val:  # Fixed typo: indorder → inorder
                return i 
        return -1

    def helper(self, preorder, inorder, left, right):
        if left > right:
            return None

        # Get the root value from preorder and move preIndex forward
        root_val = preorder[self.preIndex]
        self.preIndex += 1
        root = TreeNode(root_val)

        # Find the index of root in inorder
        indx = self.search(inorder, left, right + 1, root_val)

        # Recursively build the left and right subtree
        root.left = self.helper(preorder, inorder, left, indx - 1)
        root.right = self.helper(preorder, inorder, indx + 1, right)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preIndex = 0
        return self.helper(preorder, inorder, 0, len(inorder) - 1)


# Helper function to print the tree in inorder to verify
def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=' ')
    print_inorder(root.right)

# ---- Test Code ----
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
root = sol.buildTree(preorder, inorder)

print("Inorder of constructed tree:")
print_inorder(root)  # Should match original inorder if tree is built correctly
