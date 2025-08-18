class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}"

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Helper function to build linked list from Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to Python list (for easy checking)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Example
list1_vals = [1, 2, 4]
list2_vals = [1, 3, 4]

list1 = build_linked_list(list1_vals)
list2 = build_linked_list(list2_vals)

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Output the merged linked list
print("Merged List:", linked_list_to_list(merged_head))
