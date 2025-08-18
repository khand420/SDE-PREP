
1. # https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
# 2. https://leetcode.com/problems/next-greater-element-i/submissions/

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n  # Initialize result list with -1
        stack = []

        for i in range(n - 1, -1, -1):  # Reverse loop from n-1 to 0
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(arr[i])

        return ans
    


arr = [6, 8, 0, 1, 3]
s = Solution().nextLargerElement(arr)
print(s)  # Output: [8, -1, 1, 3, -1]












# Sure! Here's the **step-by-step approach** to solving the **Next Greater Element** problem using a **monotonic stack**.

# ---

# ## 🧠 Problem Statement

# Given an array `arr`, for each element, find the **next greater element to its right**.
# If no such element exists, return `-1` for that index.

# ---

# ## ✅ Example

# ### Input:

# ```
# arr = [6, 8, 0, 1, 3]
# ```

# ### Output:

# ```
# [8, -1, 1, 3, -1]
# ```

# ---

# ## 🧰 Tools Used

# * **Stack**: To keep track of potential next greater elements.
# * **Result array**: Initialize with `-1`s since the default is "no next greater".

# ---

# ## 🔁 Step-by-Step Approach

# ### Step 1: Initialization

# * Create a `stack` (empty).
# * Create an array `ans` of size `n` filled with `-1`.

# ### Step 2: Traverse the array **from right to left**

# * Loop from `i = n-1` to `0`.

# ### Step 3: For each `arr[i]`, do the following:

# 1. **Pop** all elements from the stack **less than or equal** to `arr[i]`.

#    * These can never be the next greater for `arr[i]` or any previous number.
# 2. If the stack is **not empty**:

#    * The top of the stack is the **next greater** element → assign it to `ans[i]`.
# 3. **Push** the current element `arr[i]` onto the stack.

#    * It might be the next greater for some element to the left.

# ---

# ## 🔂 Loop Trace (for `[6, 8, 0, 1, 3]`)

# | i | arr\[i] | Stack before | Stack after | ans\[i] |
# | - | ------- | ------------ | ----------- | ------- |
# | 4 | 3       | \[]          | \[3]        | -1      |
# | 3 | 1       | \[3]         | \[3, 1]     | 3       |
# | 2 | 0       | \[3, 1]      | \[3, 1, 0]  | 1       |
# | 1 | 8       | \[3, 1, 0]   | \[8]        | -1      |
# | 0 | 6       | \[8]         | \[8, 6]     | 8       |

# ---

# ## ⏱ Time and Space Complexity

# | Metric           | Value                     |
# | ---------------- | ------------------------- |
# | Time Complexity  | O(n)                      |
# | Space Complexity | O(n) for stack and output |

# ---

# Let me know if you want the **Next Smaller Element** version or a **circular array** variant (like for Next Greater Element II)!

