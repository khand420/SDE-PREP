
# 🐸 Frog 2 – Problem Statement
# Now, the frog can jump up to k steps ahead instead of just 1 or 2.

# 🔍 Objective:
# Still minimize the cost to reach the last step.



# # 🔁 1. **Memoization (Top-Down)**
def frog2(i, heights, k):
    memo={}
    if i == 0:
        return 0
    if i in memo:
        return memo[i]

    min_cost = float('inf')

    for j in range(1, k+1):
        if i - j >= 0:
            cost = frog2(i - j, heights, k) + abs(heights[i] - heights[i - j])
            min_cost = min(min_cost, cost)

    memo[i] = min_cost
    return memo[i]


## 📋 2. **Tabulation (Bottom-Up)**xx
# def frog2(n,h, k):
#     n = len(h)
#     dp = [float('inf')] * n
#     dp[0] = 0

#     for i in range(1, n):
#         for j in range(1, k+1):
#             if i - j >= 0:
#                 dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

#     return dp[-1]



heights = [10, 30, 40, 50, 20]
k = 3
n = len(heights)
print(frog2(n - 1, heights, k))  # Output: 30
