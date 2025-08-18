class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None
        current = root

        # Step 1: Find the node with key
        while current:
            if current.val == key:
                break
            elif current.val > key:
                successor = current
                current = current.left
            else:
                predecessor = current
                current = current.right

        # Step 2: If node with key is found
        if current:
            # Predecessor: Rightmost node in left subtree
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                predecessor = temp

            # Successor: Leftmost node in right subtree
            if current.right:
                temp = current.right
                while temp.left:
                    temp = temp.left
                successor = temp

        return (predecessor.val if predecessor else None,
                successor.val if successor else None)



#         20
#        /  \
#      10    30
#     / \    / \
#    5  15  25  35


root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

sol = Solution()
pre, suc = sol.findPreSuc(root, 15)
print("Predecessor:", pre)  # 10
print("Successor:", suc)    # 20
