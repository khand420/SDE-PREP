class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def levelorder(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    



# Build the tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)

sol = Solution()
print("Inorder:", sol.inorder(tree))     # [4, 2, 5, 1, 3, 6]
print("Preorder:", sol.preorder(tree))   # [1, 2, 4, 5, 3, 6]
print("Postorder:", sol.postorder(tree)) # [4, 5, 2, 6, 3, 1]
print("Levelorder:", sol.levelorder(tree)) # [1, 2, 3, 4, 5, 6]