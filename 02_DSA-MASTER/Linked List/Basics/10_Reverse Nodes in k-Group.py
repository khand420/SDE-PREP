# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        temp = head
        count = 0
        while count < k:
            if not temp:
                return head  # Less than k nodes remaining
            temp = temp.next
            count += 1

        # Recursively process the rest of the list
        prevNode = self.reverseKGroup(temp, k)

        # Reverse the current k nodes
        temp = head
        count = 0
        while count < k:
            next_node = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = next_node
            count += 1

        return prevNode

# Helper function to build a linked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# === Test the solution ===
if __name__ == "__main__":
    # Input list and k
    values = [1, 2, 3, 4, 5]
    k = 2

    # Build list
    head = build_linked_list(values)

    print("Original list:")
    print_linked_list(head)

    # Apply reverseKGroup
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)

    print(f"List after reversing every {k} nodes:")
    print_linked_list(new_head)






# ✅ Problem Summary
# Given a singly linked list, reverse the nodes of the list k at a time and return the modified list. If the number of nodes is not a multiple of k, leave the last remaining nodes as-is.

# 🧠 Step-by-Step Approach (Recursive Solution)

# 🔹 Step 1: Check if there are at least k nodes to reverse
# * Start with a temporary pointer (temp = head) and a counter.
# * Traverse k nodes ahead.
# * If there are fewer than k nodes, return head as-is (don’t reverse).

# 🔹 Step 2: Recursively process the rest of the list
# * After confirming the current group has at least k nodes, move temp k steps forward.
# * Recursively call reverseKGroup(temp, k) to process and reverse the rest of the list.
# * The returned node will be the head of the already processed (reversed) part.

# 🔹 Step 3: Reverse the current group of k nodes
# * Use a standard in-place linked list reversal technique for k nodes.
# * For each node in the group:
#     * Save next_node = curr.next
#     * Reverse the pointer: curr.next = prevNode
#     * Move prevNode and curr forward
# * The prevNode becomes the new head of the current group.

# 🔹 Step 4: Return the new head
# * Return prevNode (the new head of the current reversed group).
# * It will get linked properly by the previous recursive call.

# 🔄 Visual Example:
# Given: 1 -> 2 -> 3 -> 4 -> 5 and k = 2
# 1. First group: reverse 1 -> 2 → becomes 2 -> 1
# 2. Recurse on 3 -> 4 -> 5
# 3. Second group: reverse 3 -> 4 → becomes 4 -> 3
# 4. Last node 5 remains as-is (less than k)
# 5. Final result: 2 -> 1 -> 4 -> 3 -> 5

# ⏱️ Time and Space Complexity
# * Time Complexity: O(N), where N is the number of nodes in the list. Every node is visited once.
# * Space Complexity: O(N/k) recursive stack calls (worst-case O(N) in deeply nested calls). Can be reduced to O(1) with an iterative solution.
