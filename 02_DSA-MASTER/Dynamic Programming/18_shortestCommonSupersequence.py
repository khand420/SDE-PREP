#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
        #  code here
        n = len(s1)
        m = len(s2)
         
        dp = [[0] * (n + 1) for _ in range(m + 1)]
         
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # FIXED: correct character comparison
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                     
        lcs = dp[m][n]
        return m + n - lcs
    



#  --- IGNORE ---# Example usage:
s1 = "AGGTAB"
s2 = "GXTXAYB"
sol = Solution()    
print(sol.shortestCommonSupersequence(s1, s2))  # Output: 9 (One shortest common supersequence is "AGXGTXAYB")  
#  --- IGNORE ---
#User function Template for python3   