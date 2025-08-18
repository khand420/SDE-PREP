class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Helper to create a linked list from a list
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test case
values = [1, 2, 3, 4, 5]
head = createLinkedList(values)

print("Original Linked List:")
printList(head)

solution = Solution()
middle = solution.middleNode(head)

print("\nMiddle Node:")
printList(middle)
