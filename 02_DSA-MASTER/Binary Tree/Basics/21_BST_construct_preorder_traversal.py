# 1008. Construct Binary Search Tree from Preorder Traversal



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def bstFromPreorder(self, preorder):
        self.i = 0
        return self.helper(preorder, float('inf'))

    def helper(self, preorder, bound):
        if self.i >= len(preorder) or preorder[self.i] > bound:
            return None

        root_val = preorder[self.i]
        self.i += 1
        root = TreeNode(root_val)

        root.left = self.helper(preorder, root.val)
        root.right = self.helper(preorder, bound)

        return root
    
    def printInOrder(self, root):
        if root:
            self.printInOrder(root.left)
            print(root.val, end=' ')
            self.printInOrder(root.right)

root = Solution()
bst = root.bstFromPreorder([8,5,1,7,10,12])
root.printInOrder(bst)