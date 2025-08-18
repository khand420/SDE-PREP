from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for _ in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Last node in level points to None
            prev.next = None

        return root





# 🌟 Helper function to print next pointers level-by-level
def print_levels_with_next(root):
    while root:
        curr = root
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        root = root.left  # move to the next level (leftmost node)


# Build the perfect binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Connect nodes
solution = Solution()
connected_root = solution.connect(root)

# Print the levels with next pointers
print("Levels with next pointers:")
print_levels_with_next(connected_root)





# #1 Optimal Solution (Recursive, O(1) extra space):
#     def connect(self, root):
#         if not root:
#             return None

#         def dfs(node):
#             if not node or not node.left:
#                 return

#             # Connect left child to right child
#             node.left.next = node.right

#             # Connect right child to next node's left child (if exists)
#             if node.next:
#                 node.right.next = node.next.left

#             # Recurse on left and right
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         return root

# # 2 Iterative Version (No recursion):
    # def connect(self, root):
    #     if not root:
    #         return None

    #     leftmost = root

    #     while leftmost.left:
    #         head = leftmost
    #         while head:
    #             # Connect children of the same parent
    #             head.left.next = head.right

    #             # Connect children across parents
    #             if head.next:
    #                 head.right.next = head.next.left

    #             head = head.next

    #         leftmost = leftmost.left

    #     return root