# The **Celebrity Problem** is a classic algorithmic problem often solved using a **stack**.

# ---

# ## 🎯 Problem Statement

# You are given a matrix `M` of size `n x n`, where:

# * `M[i][j] == 1` means **person `i` knows person `j`**
# * `M[i][j] == 0` means **person `i` does NOT know person `j`**

# A **celebrity** is defined as:

# * Everyone **knows** the celebrity
# * The celebrity **knows no one**

# You need to find the **index of the celebrity**, or `-1` if no celebrity exists.

# ---

# ## ✅ Stack-Based Approach

# ### 🔍 Idea

# * Push all people onto a stack.
# * Pop two people at a time and compare:

#   * If `A` knows `B`, then `A` **can't** be a celebrity → discard `A`
#   * Else `B` **can't** be a celebrity → discard `B`
# * At the end, only **1 candidate** is left in the stack → check if they’re actually a celebrity.

# ---

# ## 📦 Steps

# 1. Push all indices (people) onto the stack.
# 2. While stack has more than 1 person:

#    * Pop `A` and `B`
#    * If `A` knows `B`, `A` can’t be celebrity → push `B`
#    * Else, `B` can’t be celebrity → push `A`
# 3. The remaining person is a **candidate**. Verify:

#    * They know **no one**: `M[candidate][j] == 0` for all `j ≠ candidate`
#    * Everyone knows them: `M[i][candidate] == 1` for all `i ≠ candidate`

# ---

# ## ✅ Python Code

# ```python
class Solution:
    def findCelebrity(self, M, n):
        stack = [i for i in range(n)]

        # Step 1: Eliminate non-celebrities
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            if M[a][b] == 1:
                # a knows b → a can't be celebrity
                stack.append(b)
            else:
                # a doesn't know b → b can't be celebrity
                stack.append(a)

        if not stack:
            return -1  # No candidate

        candidate = stack.pop()

        # Step 2: Validate candidate
        for i in range(n):
            if i != candidate:
                if M[candidate][i] == 1 or M[i][candidate] == 0:
                    return -1

        return candidate
    


sol = Solution()
M = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]
n = 3
print(sol.findCelebrity(M, n))  # Output: 2 (person 2 is  celebrity)  




# ```

# ---

# ## 🧪 Example

# ```python
# M = [
#     [0, 1, 1],
#     [0, 0, 1],
#     [0, 0, 0]
# ]
# n = 3

# Output: 2  # person 2 is celebrity
# ```

# ---

# ## ⏱ Time & Space Complexity

# | Metric | Value |
# | ------ | ----- |
# | Time   | O(n)  |
# | Space  | O(n)  |

# Let me know if you want to try the **2-pointer approach** for even better space!
