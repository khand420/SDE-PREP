class Solution:
    # def LongestRepeatingSubsequence(self, s):
    #     # Code here
    #     dp = {}
        
    #     def solve(s1, s2, n, m):
    #         if n == 0 or m == 0:
    #             return 0
                
    #         if (n, m) in dp:
    #             return dp[(n, m)]
                
    #         if s1[n - 1] == s2[m - 1] and n != m:
    #             c = 1 + solve(s1, s2, n - 1, m - 1)
    #         else:
    #             c1 = solve(s1, s2, n - 1, m)
    #             c2 = solve(s1, s2, n, m - 1)
    #             c = max(c1, c2)
                
    #         dp[(n, m)] = c
    #         return c
        
    #     return solve(s, s, len(s), len(s))

    
    def LongestRepeatingSubsequence(self, s1):
        # Code here
        s2 = s1
        
        n = len(s1)
        m = len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1] and i!=j:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]





# s = "aab"
sol = Solution()
print(sol.LongestRepeatingSubsequence("axxxy"))  # ✅ Output: 2

