def unique_paths(m, n):
    # Create a 2D DP array
    dp = [[1] * n for _ in range(m)]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

# Example usage
m = 3
n = 7
result = unique_paths(m, n)
print(f"The number of unique paths in a {m}x{n} grid is: {result}")
