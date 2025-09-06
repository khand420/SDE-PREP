def longestCommonSubsequence(a, b):
    # Get the lengths of the two input sequences
    n = len(a)
    m = len(b)
    
    # Initialize the DP table with 0s, size (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the DP table using the LCS relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:  # Characters match
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Now reconstruct the LCS from the DP table
    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:  # Match found, part of LCS
            ans.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:  # Move upwards if dp[i-1][j] is larger
            i -= 1
        else:  # Otherwise, move left
            j -= 1

    # Return the LCS in correct order (since it was built backwards)
    return ans[::-1]



# Example usage:
a = "AGGTAB"
b = "GXTXAYB"

# a = 1 2 3 4 1
# b = 3 4 1 2 1 3
print(longestCommonSubsequence(a, b))  # Output: ['G', 'T', 'A', 'B']       