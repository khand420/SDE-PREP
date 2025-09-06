class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # Each number is a LIS of length 1

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))           # Output: 4
print(s.lengthOfLIS([7, 7, 7, 7]))                 # Output: 1







# class Solution:
#     def lengthOfLIS(self, nums):
#         from functools import lru_cache

#         n = len(nums)

#         @lru_cache(None)
#         def dfs(i, prev_index):
#             if i == n:
#                 return 0

#             # don't take nums[i]
#             length = dfs(i + 1, prev_index)

#             # take nums[i] if it's increasing
#             if prev_index == -1 or nums[i] > nums[prev_index]:
#                 length = max(length, 1 + dfs(i + 1, i))

#             return length

#         return dfs(0, -1)




# s = Solution()
# print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4










# Here's the **step-by-step approach** to solve the **Longest Increasing Subsequence (LIS)** using **recursion**, and then with **memoization**.

# ---

# ## ✅ Problem Summary:

# > Given an array of integers `nums`, find the length of the **longest increasing subsequence** (LIS).

# ---

# ## 🔁 Recursive Approach (Top-Down)

# ### 🔹 Intuition:

# At every index `i`, we have two choices:

# 1. **Pick** the current number `nums[i]` if it is greater than the previous picked number (`nums[prev_index]`).
# 2. **Skip** the current number and move to the next index.

# We explore both choices and return the maximum length from all possible paths.

# ---

# ## 🧠 Step-by-Step Approach:

# ### Step 1: Define a recursive function

# Create a recursive function `dfs(i, prev_index)` where:

# * `i` is the current index in the array.
# * `prev_index` is the index of the last number taken in the subsequence.

# ### Step 2: Base Case

# If `i` reaches the end of the array, return 0.

# ### Step 3: Recursive Calls

# * Option 1: Skip `nums[i]` → `dfs(i + 1, prev_index)`
# * Option 2: Take `nums[i]` if it's increasing → `1 + dfs(i + 1, i)`

# ### Step 4: Return the max of both options

# ---

# ## 📦 Optimization with Memoization

# Since there are overlapping subproblems (same `i` and `prev_index` pairs), use **memoization** to avoid redundant work.

# You can use:

# * `@lru_cache` decorator in Python, or
# * a 2D `dp` table.

# ---

# ## 📌 Example Code with Memoization

# ```python
# class Solution:
#     def lengthOfLIS(self, nums):
#         from functools import lru_cache
#         n = len(nums)

#         @lru_cache(None)
#         def dfs(i, prev_index):
#             if i == n:
#                 return 0

#             # skip current number
#             not_take = dfs(i + 1, prev_index)

#             # take current number if valid
#             take = 0
#             if prev_index == -1 or nums[i] > nums[prev_index]:
#                 take = 1 + dfs(i + 1, i)

#             return max(take, not_take)

#         return dfs(0, -1)
# ```

# ---

# ## ⏱️ Time Complexity:

# * **O(n²)** — because we cache results for each pair of `i` and `prev_index`.
# * **O(n²)** space (memoization table).

# ---

# ## 📌 Summary

# | Step | Description                                    |
# | ---- | ---------------------------------------------- |
# | 1    | Define recursive function `dfs(i, prev_index)` |
# | 2    | At each step, try both options: take or skip   |
# | 3    | Use memoization to cache results               |
# | 4    | Return the maximum length from index 0         |

# ---

# Let me know if you want the **tabulation** or **binary search (O(n log n))** version too.
