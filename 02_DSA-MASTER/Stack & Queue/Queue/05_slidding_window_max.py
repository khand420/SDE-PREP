from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        # Process first k elements (first window)
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        # Process the rest of the elements
        for i in range(k, len(nums)):
            res.append(nums[dq[0]])  # Add max of previous window

            # Remove elements not in current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove elements smaller than current
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

        # Add max for the last window
        res.append(nums[dq[0]])

        return res


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3, 3, 5, 5, 6, 7]
# print(sol.maxSlidingWindow([1], 1))  # Output: [1]
# print(sol.maxSlidingWindow([1, -1], 1))  # Output: [1, -1]
# print(sol.maxSlidingWindow([9, 7, 8, 2, 3, 6, 5], 3))  # Output: [9, 8, 8, 6]
# print(sol.maxSlidingWindow([4, 3, 5, 2, 6, 2], 3))  # Output: [5, 5, 6]



# ✅ Problem Statement (Leetcode 239)
# You are given an integer array nums and an integer k, a sliding window size. Return a list of the maximum value in every contiguous subarray of size k.

# 🔍 Example
# python
# Copy
# Edit
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
# Output: [3,3,5,5,6,7]
# Each window:

# [1,3,-1] → 3

# [3,-1,-3] → 3

# [-1,-3,5] → 5

# [-3,5,3] → 5

# [5,3,6] → 6

# [3,6,7] → 7

# ⚙️ Optimal Approach (Using Deque)
# We use a deque (double-ended queue) to keep track of indices of useful elements in decreasing order.

# ✅ Step-by-Step Breakdown
# Initialize:

# An empty deque dq to store indices (not values).

# An empty list res to store results.

# Process the first k elements (first window):

# For each index i in the first k elements:

# While deque is not empty and current value > value at back of deque, pop from back.

# Append current index to deque.

# Process the rest of the array:
# For each index i from k to len(nums):

# The element at front of deque is the max of the previous window. Add it to res.

# Remove indices from front if they are out of the current window (dq[0] <= i - k).

# Remove indices from back if their values are less than the current value.

# Append the current index.

# After loop ends, append the max of the last window (nums[dq[0]]) to res.



# 📊 Time & Space Complexity
# Metric	Complexity
# Time	O(n)
# Space (deque)	O(k)
# Output space	O(n - k + 1)

# Why O(n)? Each element is added and removed from the deque at most once.

# 🧠 Key Takeaways
# Deque stores indices, not values.

# It maintains a monotonically decreasing order of values (from front to back).

# Always remove:

# From front if it's outside the window.

# From back if value is smaller than current