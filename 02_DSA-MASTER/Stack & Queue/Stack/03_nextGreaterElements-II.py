class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            curr = i % n
            while stack and nums[stack[-1]] <= nums[curr]:
                stack.pop()

            if i < n:
                if stack:
                    res[curr] = nums[stack[-1]]

            stack.append(curr)

        return res


sol = Solution()
# nums = [1, 2, 1]
nums = [1,2,3,4,3]
result = sol.nextGreaterElements(nums)
print(result)  # Output: [2, -1, 2] [2,3,4,-1,4]



# ✅ Approach: Monotonic Stack + Circular Loop
# Since the array is circular, we simulate two passes of the array using modulo:

# Step-by-step:
# Initialize:

# n = len(nums)

# res = [-1] * n (default values)

# stack = [] (stores indices, not values)

# Traverse the array twice (from 2n - 1 to 0):

# Use i % n to get the actual index in the circular array.

# While stack is not empty and nums[stack[-1]] <= nums[i % n]: pop

# If i < n:

# If stack is not empty → res[i] = nums[stack[-1]]

# Push i % n to the stack