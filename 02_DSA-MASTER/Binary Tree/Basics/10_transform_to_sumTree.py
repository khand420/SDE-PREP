class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
    
def sum_nodes(root):
    if not root:
        return 0
    leftSum = sum_nodes(root.left) 
    rihghtSum = sum_nodes(root.right)
    root.val += leftSum + rihghtSum
    return root.val



# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5


print("Before transformation:")
preorder(root) 
print("\n", "Sum of all nodes:",sum_nodes(root) ,"\n")  
print("after transformation:") 
preorder(root)  

