class Solution:
    def lcs(self, s1, s2):
        # code here
        n1 = len(s1)
        n2 = len(s2)
        
        # dp = {}
        # def solve(s1,s2,n1, n2):
        #     if n1 == 0 or n2 == 0:
        #         return 0
                
        #     elif (n1,n2) in dp:
        #         return dp[(n1,n2)]
            
        #     else:
        #         if s1[n1-1] == s2[n2-1]:
        #             c = 1+solve(s1, s2, n1-1, n2-1)
        #         else:
        #             c1 = solve(s1, s2, n1-1, n2)
        #             c2 = solve(s1, s2, n1, n2-1)
        #             c = max(c1, c2)
                
        #         dp[n1,n2] = c
        #         return c
        # return solve(s1,s2,n1, n2)


                # 1. Tabulation: Initialize a (n1+1) x (n2+1) DP table
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        # Fill the DP table
        for i in range(1, n1 + 1):  # Loop through s1
            for j in range(1, n2 + 1):  # Loop through s2
                if s1[i - 1] == s2[j - 1]:  # If characters match
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:  # If characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Return the final result from the DP table
        return dp[n1][n2]
                    
                    


sol = Solution()
print(sol.lcs("ABCDGH", "AEDFHR"))  # Output: 3
print(sol.lcs("AGGTAB", "GXTXAYB"))  # Output: 4