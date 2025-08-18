
# The Morris Inorder Traversal is a way to traverse a binary tree in-order without using recursion or a stack. It uses a technique called threaded binary trees, temporarily modifying the tree structure to keep track of where to return after visiting the left subtree.

# ✅ Problem: Morris Inorder Traversal of a Binary Tree
# Goal: Traverse the binary tree in inorder (left → root → right) with O(1) space (excluding output).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        current = root

        while current:
            if current.left is None:
                # Visit current node
                result.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor of current
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right

                if pre.right is None:
                    # Create a thread to current
                    pre.right = current
                    current = current.left
                else:
                    # Remove the thread and visit current
                    pre.right = None
                    result.append(current.val)
                    current = current.right

        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.inorderTraversal(root))