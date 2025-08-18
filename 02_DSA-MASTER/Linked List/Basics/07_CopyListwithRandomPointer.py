class Node(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Dictionary to hold old nodes as keys and new nodes as values
        old_to_new = {}

        # First pass: create copy of all nodes without assigning next/random
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers
        current = head
        while current:
            clone = old_to_new[current]
            clone.next = old_to_new.get(current.next)
            clone.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]



def print_list(head):
    nodes = []
    while head:
        rand = head.random.val if head.random else None
        nodes.append(f"[Val: {head.val}, Rand: {rand}]")
        head = head.next
    print(" -> ".join(nodes))

# Create original list: 1 -> 2
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node1.random = node2
node2.random = node2

solution = Solution()
copied = solution.copyRandomList(node1)
print_list(copied)
