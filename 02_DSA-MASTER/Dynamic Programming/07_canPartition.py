# Partition Equal Subset Sum

class Solution:
    # def canPartition(self, nums):
        # total = sum(nums)
        
        # # If total sum is odd, cannot partition into equal subsets
        # if total % 2 != 0:
        #     return False
        
        # target = total // 2
        # n = len(nums)
        # memo = {}

        # def dfs(i, current_sum):
        #     # If current_sum == target, we found a valid subset
        #     if current_sum == target:
        #         return True

        #     # If out of bounds or sum exceeds target, stop
        #     if i >= n or current_sum > target:
        #         return False

        #     # Memoization key
        #     key = (i, current_sum)
        #     if key in memo:
        #         return memo[key]

        #     # Choose to include nums[i] or not
        #     include = dfs(i + 1, current_sum + nums[i])
        #     exclude = dfs(i + 1, current_sum)

        #     memo[key] = include or exclude
        #     return memo[key]

        # return dfs(0, 0)



    def canPartition(self, nums):
        total = sum(nums)
        
        # Can't split if total is odd
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        # dp[i][j] = True if we can make sum j using first i elements
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Sum 0 is always possible with empty subset
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(target + 1):
                if nums[i - 1] <= j:
                    # Include or exclude nums[i - 1]
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    # Cannot include nums[i - 1]
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]


sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))  # True → subsets: [1, 5, 5] and [11]
print(sol.canPartition([1, 2, 3, 5]))   # False
