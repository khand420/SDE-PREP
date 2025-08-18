# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.nextRight = None  # initialize as None

    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if root is None:
            return

        # Recur on right and left subtrees in reverse order
        self.flatten(root.right)
        self.flatten(root.left)

        # Rearrange pointers
        root.left = None
        root.right = self.nextRight

        # Move nextRight to current node
        self.nextRight = root

def printFlattenedTree(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
solution.flatten(root)
printFlattenedTree(root)