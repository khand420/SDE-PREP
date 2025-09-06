#User function Template for python3
import sys 
sys.setrecursionlimit(5000)

class Solution:
    def knapSack(self, val, wt, cap):
        dp = {}
        N = len(val)

        def solve(n, cap):
            if n == 0 or cap == 0:
                return 0

            if (n, cap) in dp:
                return dp[(n, cap)]

            cw = wt[n - 1]
            cv = val[n - 1]

            if cw <= cap:
                c1 = cv + solve(n, cap - cw)     # pick the same item again
                c2 = solve(n - 1, cap)            # skip the item
                c = max(c1, c2)
            else:
                c = solve(n - 1, cap)

            dp[(n, cap)] = c
            return c

        return solve(N, cap)


# # ✅ 1. Tabulation (2D DP) – Bottom-Up
# class Solution:
#     def knapSack(self, val, wt, cap):
#         n = len(val)
#         dp = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]

#         for i in range(1, n + 1):
#             for j in range(cap + 1):
#                 if wt[i - 1] <= j:
#                     # pick (again) or don't pick
#                     dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j])
#                 else:
#                     # can't pick
#                     dp[i][j] = dp[i - 1][j]

#         return dp[n][cap]


# # ✅ 2. Space Optimized (1D DP)
# # You only need dp[cap + 1] since at each step, you're only using values from the same row.
# class Solution:
#     def knapSack(self, val, wt, cap):
#         n = len(val)
#         dp = [0 for _ in range(cap + 1)]

#         for i in range(n):
#             for j in range(wt[i], cap + 1):
#                 dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

#         return dp[cap]



sol = Solution()
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]
cap = 8
print(sol.knapSack(val, wt, cap))  # Expected output: 110
