 # 1, 2 DP Tabulation
class Solution:
    # def MinCoin(self, nums, amount):
    #     n = len(nums)
    #     nums.sort(reverse=True)  # Optional: prioritizes larger coins
    #     dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]

    #     # Base case: 0 coins are needed to make amount 0
    #     for i in range(n + 1):
    #         dp[i][0] = 0

    #     for i in range(1, n + 1):
    #         for j in range(1, amount + 1):
    #             val = nums[i - 1]
    #             if val <= j:
    #                 c1 = 1 + dp[i][j - val]  # take the coin
    #                 c2 = dp[i - 1][j]        # skip the coin
    #                 dp[i][j] = min(c1, c2)
    #             else:
    #                 dp[i][j] = dp[i - 1][j]  # should not skip this

    #     val = dp[n][amount]
    #     if val == float("inf"):  # If no solution was found, return -1
    #         return -1
    #     else:
    #         return val

    def MinCoin(self, nums, amount):
        # 1DP Tabulation
        # way 1
        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # way 2
        dp = [0] * (amount + 1)
        nums.sort()  # Optional: Sorting ensures we try smaller coins first 
        #  way 1
        # for coin in nums:
        #     for j in range(coin, amount + 1):
        #         dp[j] = min(dp[j], 1 + dp[j - coin])

        # way 2
        for amt in range(1, amount + 1):
            ans = float("inf")
            for coin in nums:
                if coin <= amt:
                    ans = min(ans, 1 + dp[amt - coin])
                else:
                    break  # No need to try larger coins
            dp[amt] = ans   # Store the result for the current amount)

        val = dp[amount]
        if val == float("inf"):  # If no solution was found, return -1
            return -1
        else:
            return val
        


 # 1, 2 DP Memoization

# class Solution:
#     def MinCoin(self, nums, amount):
#         # 1DP Memoization
#         dp = {}
#         nums.sort()  # Optional: Sorting ensures we try smaller coins first

#         def solve(amount):
#             if amount == 0:
#                 return 0
#             elif amount in dp:
#                 return dp[amount]

#             ans = float("inf")
#             for coin in nums:
#                 if coin <= amount:
#                     ans = min(ans, 1 + solve(amount - coin))  # Recursive call
#                 else:
#                     break  # No need to try larger coins

#             dp[amount] = ans  # Store the result for the current amount
#             return ans

#         val = solve(amount)
#         if val == float("inf"):  # If no solution was found, return -1
#             return -1
#         else:
#             return val

        
        
        # 		2DP
        # n = len(nums)
        # nums.sort(reverse=True)  # Optional: prioritizes larger coins
        # dp = {}

        # def solve(n, amount):
        #     if amount == 0:
        #         return 0
        #     elif n == 0:
        #         return float("inf")
        #     elif (n, amount) in dp:
        #         return dp[(n, amount)]
        #     else:
        #         val = nums[n - 1]
        #         if val <= amount:
        #             c1 = 1 + solve(n, amount - val)  # take the coin
        #             c2 = solve(n - 1, amount)        # skip the coin
        #             c = min(c1, c2)
        #         else:
        #             c = solve(n - 1, amount)         # ✅ should not skip this
        #         dp[(n, amount)] = c
        #         return c

        # val = solve(n, amount)
        # if val == float("inf"):  # ✅ use this instead of 10**9+7
        #     return -1
        # else:
        #     return val



sol = Solution()
print(sol.MinCoin([1, 2, 5], 11))  # Output: 3
print(sol.MinCoin([2], 3))         # Output: -1
print(sol.MinCoin([1], 0))         # Output: 0
print(sol.MinCoin([1], 1))         # Output: 1