# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                # Save the next node
                next_node = curr.next

                # Flatten the child list
                child_head = self.flatten(curr.child)

                # Insert child between curr and next_node
                curr.next = child_head
                child_head.prev = curr
                curr.child = None  # Don't forget to remove the child pointer

                # Traverse to the tail of the flattened child list
                tail = child_head
                while tail.next:
                    tail = tail.next

                # Reconnect the saved next_node
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail

            curr = curr.next

        return head
def print_list(head):
    curr = head
    while curr:
        print(f"Node({curr.val})", end=" <-> ")
        if curr.child:
            print(f"Child({curr.child.val})", end=" ")
        curr = curr.next
    print("None")   



# Example usage
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next

head.next.child = Node(4)
head.next.child.next = Node(5)
head.next.child.next.prev = head.next.child 

flattened_head = Solution().flatten(head)

# 🖨️ This was missing
print_list(flattened_head)