# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def all_path(self, root, path, ans):
        if root.left is None and root.right is None:
            ans.append(path)
            return 
        if root.left:
            self.all_path(root.left,path+"->"+str(root.left.val), ans)
        if root.right:
            self.all_path(root.right,path+"->"+str(root.right.val), ans)

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []
        path = str(root.val)
        self.all_path(root, path, ans)
        return ans
    

Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(3)
Tree.left.left = TreeNode(4)
Tree.left.right = TreeNode(5)

sol = Solution()
print(sol.binaryTreePaths(Tree))