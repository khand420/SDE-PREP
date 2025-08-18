# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # def swapPairs(self, head):
        
    #     if not head or not head.next:
    #         return head
        
    #     first= head
    #     second = head.next
    #     prev = None

    #     while first and second:
    #         third = second.next
    #         second.next = first
    #         first.next = third
            
    #         if prev:
    #             prev.next = second
    #         else:
    #             head = second

    #         # update
    #         prev = first
    #         first = third
    #         if third:
    #             second = third.next
    #         else:
    #             second = None
                
    #     return head



    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        # Swap the rest recursively
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second


# Helper function to build a linked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head 

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")   


# === Test the solution ===
if __name__ == "__main__":
    # Input list
    values = [1, 2, 3, 4, 5]

    # Build list
    head = build_linked_list(values)

    print("Original list:")
    print_linked_list(head)

    # Swap pairs
    solution = Solution()
    swapped_head = solution.swapPairs(head)

    print("List after swapping pairs:")
    print_linked_list(swapped_head) 





# Problem Summary
# Given the head of a singly linked list, swap every two adjacent nodes and return its head. You must perform the swap by changing the node connections (not just values).

# 🧠 Step-by-Step Approach (Recursive & Iterative Available)
# Let's cover the recursive approach first, then briefly mention the iterative one.

# 🔁 Recursive Approach

# 🔹 Step 1: Base Case Check
# * If the list is empty (head is None) or only one node remains (head.next is None), there’s nothing to swap.
# * Return head as-is.

# 🔹 Step 2: Identify the First Two Nodes
# * first = head
# * second = head.next
# These are the two nodes to be swapped.

# 🔹 Step 3: Recursively Swap the Rest of the List
# * Call self.swapPairs(second.next) — this swaps the remaining list starting from the third node.
# * Attach the returned node to first.next — connecting the swapped rest to the first node.

# 🔹 Step 4: Perform the Swap
# * second.next = first
# * first.next = recursively swapped head
# * Return second as the new head of this pair.

# 🧩 Visual Example:
# For input: 1 -> 2 -> 3 -> 4
# Recursive steps:
# 1. Swap 1 and 2 → 2 -> 1
# 2. Recursively call on 3 -> 4
# 3. Swap 3 and 4 → 4 -> 3
# 4. Connect: 2 -> 1 -> 4 -> 3

# ✅ Final Recursive Structure
# python
# CopyEdit
# class Solution:
#     def swapPairs(self, head):
#         if not head or not head.next:
#             return head
        
#         first = head
#         second = head.next
        
#         # Swap the rest recursively
#         first.next = self.swapPairs(second.next)
#         second.next = first
        
#         return second

# 🔄 Iterative (Optional)
# Use a dummy node and a loop to swap in place:
# 1. Initialize dummy = ListNode(0) and point dummy.next = head.
# 2. Use a pointer prev to track the node before the pair.
# 3. Loop through the list in pairs and swap nodes using prev, first, and second.

# ⏱️ Time & Space Complexity
# * Time Complexity: O(N) — each node is visited once.
# * Space Complexity:
#     * Recursive: O(N) due to the recursion stack
#     * Iterative: O(1) (no extra space used)
