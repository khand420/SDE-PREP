#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s1):
        # code here
        s2 = s1[::-1]
        n = len(s1)
        m = len(s2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][m]
    
    # solve this in 1 dp array only
    # def longestPalinSubseq(self, s1):
    #     # code here    
        # n = len(s1)    
        # dp = [0]*(n+1)                    
        # for i in range(n-1, -1, -1):
        #     prev = 0
        #     for j in range(i, n):
        #         temp = dp[j]
        #         if s1[i] == s1[j]:
        #             dp[j] = 2 + prev if i != j else 1
        #         else:
        #             dp[j] = max(dp[j], dp[j-1])
        #         prev = temp
        # return dp[n-1]
    


sol = Solution()
print(sol.longestPalinSubseq("bbabcbcab"))  # Output: 7
print(sol.longestPalinSubseq("abcd"))  # Output: 1
print(sol.longestPalinSubseq("a"))  # Output: 1
print(sol.longestPalinSubseq("aa"))  # Output: 2