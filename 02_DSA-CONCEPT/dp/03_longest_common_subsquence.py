# def lcs_recursive(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     if X[m - 1] == Y[n - 1]:
#         return 1 + lcs_recursive(X, Y, m - 1, n - 1)
#     else:
#         return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))



# def lcs_dp(X, Y):
#     m = len(X)
#     n = len(Y)
    
#     # Create a DP table to store lengths of LCS
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    
#     # Fill the DP table
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
#     return dp[m][n]




# X = "AGGTAB"
# Y = "GXTXAYB"

# print("Length of LCS (Recursive):", lcs_recursive(X, Y, len(X), len(Y)))
# print("Length of LCS (DP):", lcs_dp(X, Y))





def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS from the DP table
    lcs_length = dp[m][n]
    lcs_subsequence = []
    
    # Backtrack to find the LCS
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_subsequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    lcs_subsequence.reverse()  # Reverse to get the correct order
    return lcs_length, lcs_subsequence



# X = "AGGTAB"
# Y = "GXTXAYB" 
X = "adgei"
Y = "abgei"


# # Using Recursive Approach
# length_recursive, subsequence_recursive = get_lcs_recursive(X, Y)
# print("Length of LCS (Recursive):", length_recursive)
# print("LCS (Recursive):", ''.join(subsequence_recursive))

# Using Dynamic Programming Approach
lcs_length, lcs_subsequence = lcs_dp(X, Y)
print("Length of LCS (DP):", lcs_length)
print("LCS (DP):", ''.join(lcs_subsequence))
