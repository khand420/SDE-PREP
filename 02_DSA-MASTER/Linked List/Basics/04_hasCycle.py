# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):

        slow = head
        fast = head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)        
node.next.next.next.next = node.next # Creating a cycle for testing purposes
solution = Solution()
print(solution.hasCycle(node))  # Should return True since there is a cycle