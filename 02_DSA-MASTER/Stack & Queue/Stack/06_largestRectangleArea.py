class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = [-1] * n
        right = [n] * n  # default to n for right boundaries
        stack = []

        # Next smaller to left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        # Next smaller to right
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Calculate max area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))  
# Output: 10 (rectangle from heights[2] to heights[3]: min height 5, width 2)





# Absolutely! Here's the **step-by-step approach** to solve the **Largest Rectangle in Histogram** problem using a **monotonic stack**.

# ---

# ## 🧠 Problem Summary

# Given an array `heights[]` where each element represents the height of a histogram bar, find the **area of the largest rectangle** that can be formed using **consecutive bars**.

# ---

# ## 🧰 Intuition

# To find the largest rectangle, for each bar `i`, we want to know:

# * **How far can we extend to the left and right** before we hit a shorter bar?

# This means:

# * Find the **first smaller element to the left** of each bar.
# * Find the **first smaller element to the right** of each bar.

# Once we have that, we can compute the **width** of the largest rectangle for each bar and find the maximum.

# ---

# ## 🧱 Step-by-Step Approach

# ### Step 1: Initialize arrays

# * `left[i]`: index of the **first smaller bar to the left** of `heights[i]`
#   → initialized with `-1`
# * `right[i]`: index of the **first smaller bar to the right** of `heights[i]`
#   → initialized with `n` (i.e., end of histogram)

# ---

# ### Step 2: Fill `left[]` using a stack

# * Traverse from left to right.
# * Maintain a stack of **indices** where the height is **monotonically increasing**.
# * For each `i`:

#   * Pop from stack while `heights[stack[-1]] >= heights[i]`.
#   * If stack is not empty → `left[i] = stack[-1]`
#   * Push `i` onto the stack.

# ---

# ### Step 3: Fill `right[]` using a stack

# * Clear the stack.
# * Traverse from right to left.
# * Maintain the same logic to find the first smaller bar to the right.

# ---

# ### Step 4: Calculate area for each bar

# * For each `i`, calculate:

#   ```
#   width = right[i] - left[i] - 1
#   area = heights[i] * width
#   ```

# * Track `max_area = max(max_area, area)`

# ---

# ### Step 5: Return `max_area`

# ---

# ## ✅ Time & Space Complexity

# | Metric | Complexity |
# | ------ | ---------- |
# | Time   | O(n)       |
# | Space  | O(n)       |

# > We traverse the list a few times and use stacks for tracking boundaries.

# ---

# ## 🧪 Example

# Given: `heights = [2,1,5,6,2,3]`

# * `left = [-1, -1, 1, 2, 1, 4]`
# * `right = [1, 6, 4, 4, 6, 6]`
# * Areas = `[2, 6, 10, 6, 8, 3]`

# → **Max Area = 10**

# ---

# Let me know if you'd like to see this visually or walk through a dry run!
