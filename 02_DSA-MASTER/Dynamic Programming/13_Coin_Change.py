class Solution:

    
    def count(self, coins, sums):
        # code here 
        n = len(coins)
        
        
   # 1. Memoization (Top-Down) Approach
    #     dp ={}
    #     def solve(n, sums):
    #         if sums == 0:
    #             return 1
                
    #         if n == 0:
    #             return 0
                
    #         elif (n, sums) in dp:
    #             return dp[(n,sums)]
                
    #         else:
    #             val = coins[n-1]
    #             if val <= sums:
    #                 c1 = solve(n, sums - val)    # include current coin (unbounded)
    #                 c2 = solve(n - 1, sums)      # exclude current coin
    #                 c = c1+c2
                    
    #             else:
    #                 c = solve(n-1, sums)
                    
    #         dp[n, sums] = c
    #         return c
            
    #     return solve(n, sums)


    # 2. Tabulation (Bottom-Up) Approach
        dp = [[0] * (sums+1) for _ in range(n+1)]     
        for i in range(n+1):
            for j in range(sums+1):
                # sums = j
                # n= i
                
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                
                else:
                    val = coins[i-1]
                    if val <= j:
                        c1 = dp[i][j-val]
                        c2 = dp[i-1][j]
                        dp[i][j] = c1+c2
                    else:
                        dp[i][j] = dp[i-1][j]
                    
        return  dp[n][sums] 
        


    

# Example usage
coins = [1, 2, 5]
amount = 11
solution = Solution()
print(solution.count(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)