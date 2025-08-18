# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # Queue stores pairs of (node, index)
        queue = deque()
        queue.append((root, 0))
        max_width = 0

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]  # First node's index in this level

            for i in range(level_length):
                node, idx = queue.popleft()
                # Normalize index to prevent overflow
                idx -= level_head_index

                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))

            # Width is last index - first index + 1
            current_width = idx + 1  # Since idx is the last node's normalized index
            max_width = max(max_width, current_width)

        return max_width



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.widthOfBinaryTree(root))