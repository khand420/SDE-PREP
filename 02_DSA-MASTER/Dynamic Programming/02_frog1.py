
# 🐸 Frog 1 – Problem Statement
# A frog is on the 1st step of n steps (0-indexed). The frog wants to reach the last step.

# Each step i has a height h[i].

# The frog can jump from step i to:

# Step i+1 (cost = abs(h[i] - h[i+1]))

# Step i+2 (cost = abs(h[i] - h[i+2]))

# 🔍 Objective:
# Minimize the total cost to reach the last step.




## 🔁 1. **Memoization (Top-Down)**
# You write a **recursive solution** and cache results.

def frog1(i, heights):
    memo={}
    if i == 0:
        return 0
    if i in memo:
        return memo[i]

    # Option 1: Jump from (i-1)
    cost = frog1(i - 1, heights) + abs(heights[i] - heights[i - 1])

    # Option 2: Jump from (i-2) if possible
    if i > 1:
        cost = min(cost, frog1(i - 2, heights) + abs(heights[i] - heights[i - 2]))

    memo[i] = cost
    return memo[i]


## 📋 2. **Tabulation (Bottom-Up)**
# You **build a table** from smaller subproblems to the final answer.

# def frog1(n, h):
#     n = len(h)
#     dp = [0] * n
#     dp[0] = 0
#     if n > 1:
#         dp[1] = abs(h[1] - h[0])

#     for i in range(2, n):
#         dp[i] = min(
#             dp[i-1] + abs(h[i] - h[i-1]),
#             dp[i-2] + abs(h[i] - h[i-2])
#         )

#     return dp[-1]


# Example usage
if __name__ == "__main__":      
    heights = [30, 10, 60, 10, 60, 50]
    n = len(heights)
    print(frog1(n - 1, heights))  # Output: 40
