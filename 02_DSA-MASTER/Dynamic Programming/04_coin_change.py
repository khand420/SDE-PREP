
# Approach (DP - Bottom-Up)
# We use DP to build the solution from 0 to amount, storing the minimum coins needed for every amount i.

# 🔹 Steps:
# Create a dp array of size amount + 1 and initialize:

# dp[0] = 0 (0 coins needed for amount 0)

# All other entries as inf (impossible by default)

# For each coin, update dp[i] for all amounts i >= coin:

# dp[i] = min(dp[i], dp[i - coin] + 1)

# After filling the table, if dp[amount] == inf, return -1 (not possible), else return dp[amount].

class Solution:
    def coinChange(self, coins, amount):
        # Step 1: Initialize dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Step 2: Build up the dp table
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Step 3: Return the result
        return dp[amount] if dp[amount] != float('inf') else -1




# class Solution:
#     def coinChange(self, coins, amount):
#         memo = {}

#         def dp(rem):
#             # Base case: exact match
#             if rem == 0:
#                 return 0
#             # Invalid case: no solution
#             if rem < 0:
#                 return float('inf')
#             # Check memo
#             if rem in memo:
#                 return memo[rem]

#             # Try all coins
#             min_coins = float('inf')
#             for coin in coins:
#                 res = dp(rem - coin)
#                 if res != float('inf'):
#                     min_coins = min(min_coins, res + 1)

#             memo[rem] = min_coins
#             return min_coins

#         result = dp(amount)
#         return result if result != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
solution = Solution()
print(solution.coinChange(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)