class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. insert
def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root


def buildBST(arr):
    root = None
    for val in arr:
        root = insertIntoBST(root, val)
    return root


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)



# 2. search 
def search(root, key):
    if root is None:
        return False
    
    if root.val == key:
        return True
    
    elif key < root.val:
        return search(root.left, key)   
    else:
        return search(root.right, key)
    


# 3. delete 0, 1, 2 children
def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node found
        # Case 0 and 1: 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 2: 2 children
        # Find inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # Copy successor value to current node
        root.val = successor.val
        # Delete successor
        root.right = deleteNode(root.right, successor.val)

    return root




# Sample input
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

# Build BST
root = buildBST(values)

# Print inorder (should be sorted)
print("Inorder Traversal of BST:")
inorderTraversal(root)
print()

# Search for key
key = 7
found = search(root, key)
print(f"Key {key} found in the BST: {found}")


# Delete key
key_to_delete = 10
root = deleteNode(root, key_to_delete)
print("Inorder Traversal after deleting key:", key_to_delete)
inorderTraversal(root)
print()