class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        ans = [0] * n
        stack = []  # Will store indices

        for i in range(n):
            # Pop elements from stack while stack top is less than or equal to current price
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack is empty, it means no greater element to the left
            if not stack:
                ans[i] = i + 1
            else:
                ans[i] = i - stack[-1]

            # Push current index to stack
            stack.append(i)

        return ans  # ✅ You were missing this



arr = [100, 80, 60, 70, 60, 75, 85]
print(Solution().calculateSpan(arr))  
# Output: [1, 1, 1, 2, 1, 4, 6]




# 📌 Step-by-Step Approach (Monotonic Stack)
# 💡 Problem Statement:
# Given an array of daily stock prices, for each day, calculate the number of consecutive days before and including today where the price was less than or equal to today's price.

# 🧠 Idea:
# We use a monotonic decreasing stack to track the indices of previous higher prices.

# For each price, we pop elements from the stack until we find a previous day with a higher price.

# The distance between the current index and the top of the stack gives us the span.

# 🔁 Steps:
# Initialize a result list ans[] of size n with zeros.

# Initialize an empty stack to store indices.

# For each price arr[i]:

# While stack is not empty and arr[stack[-1]] <= arr[i], pop from stack.

# If stack is empty → span is i + 1 (no higher value to the left)

# Else → span is i - stack[-1]

# Push i to stack.

# Return ans[].

# ⏱️ Time Complexity:
# O(n): Each index is pushed and popped from the stack at most once.