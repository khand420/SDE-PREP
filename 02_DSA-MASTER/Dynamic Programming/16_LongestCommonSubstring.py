class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        
        dp = [[0]*(m+1) for _ in range(n+1)]  # Initialize DP table
        
        ans = 0  # Variable to track the longest common substring length
        for i in range(1, n+1):  # Loop through s1
            for j in range(1, m+1):  # Loop through s2
                if s1[i-1] == s2[j-1]:  # Check if characters match
                    dp[i][j] = 1 + dp[i-1][j-1]  # Increment length of common substring
                    ans = max(ans, dp[i][j])  # Update answer
                else:
                    dp[i][j] = 0  # If characters don't match, reset dp[i][j] to 0
        
        return ans  # Return the length of the longest common substring
