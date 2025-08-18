# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head 
        is_cycle = False
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
               is_cycle = True
               break

        if not is_cycle:
            return None
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
        
node = ListNode(3)
node.next = ListNode(2)        
node.next.next = ListNode(0)        
node.next.next.next = ListNode(-4)        
node.next.next.next.next = node.next # Creating a cycle for testing purposes
solution = Solution()        
# print(solution.detectCycle(node))  # Should return the node with value 2, which is the start of the cycle   
print(solution.detectCycle(node).val)




# # Helper to create the linked list and cycle
# def create_linked_list_with_cycle(values, pos):
#     if not values:
#         return None

#     head = ListNode(values[0])
#     current = head
#     cycle_entry = None

#     for index in range(1, len(values)):
#         current.next = ListNode(values[index])
#         current = current.next
#         if index == pos:
#             cycle_entry = current

#     if pos == 0:
#         cycle_entry = head

#     # Connect tail to cycle_entry
#     current.next = cycle_entry

#     return head

# # Example usage
# values = [3, 2, 0, -4]
# pos = 1

# head = create_linked_list_with_cycle(values, pos)
# solution = Solution()
# cycle_start_node = solution.detectCycle(head)

# if cycle_start_node:
#     # Find index of cycle start node
#     current = head
#     index = 0
#     while current != cycle_start_node:
#         current = current.next
#         index += 1
#     print(f"tail connects to node index {index}")
# else:
#     print("no cycle")