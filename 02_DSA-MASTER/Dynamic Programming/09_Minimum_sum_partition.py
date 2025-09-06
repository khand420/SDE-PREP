class Solution:
    # def minDifference(self, arr):
    #     # ✅ Fix 1: You should not subtract 1 here
    #     N = len(arr)
    #     summ = sum(arr)
    #     dp = {}

    #     def solve(n, p1, summ):
    #         p2 = summ - p1

    #         # ✅ Fix 2: You need to stop when n == 0 (not access n-1 beyond that)
    #         if n == 0:
    #             return abs(p1 - p2)  # ✅ Fix 3: Return absolute difference

    #         elif (n, p1) in dp:
    #             return dp[(n, p1)]

    #         else:
    #             item = arr[n - 1]  # ✅ Now safe to access arr[n-1]

    #             # ✅ Fix 4: Remove this logic; instead always try both include/exclude
    #             c1 = solve(n - 1, p1 - item, summ)  # include item in subset
    #             c2 = solve(n - 1, p1, summ)         # exclude item

    #             c = min(c1, c2)

    #         dp[(n, p1)] = c
    #         return c

    #     return solve(N, summ, summ)  # ✅ Call with full size and full sum



     def minDifference(self, arr):
        n = len(arr)
        total = sum(arr)
        
        # dp[i][j] = True if sum j is possible with first i elements
        dp = [[False] * (total + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True  # sum 0 is always possible
        
        for i in range(1, n + 1):
            for j in range(total + 1):
                if j >= arr[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Find the minimum difference
        min_diff = float('inf')
        for j in range(total // 2 + 1):
            if dp[n][j]:
                min_diff = min(min_diff, abs(total - 2 * j))
        
        return min_diff
     


# Example usage
arr = [1, 6, 11, 5]
solution = Solution()
print(solution.minDifference(arr))  # Output: 1