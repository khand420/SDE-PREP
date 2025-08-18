def knapsack(weights, values, W):
    n = len(values)
    
    # Create a 2D array to store the maximum value at each n and W
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value will be in the last cell
    return dp[n][W]

# Example usage
weights = [1, 2, 3, 5]
values = [1, 6, 10, 16]
W = 7

max_value = knapsack(weights, values, W)
print(f"The maximum value that can be obtained is: {max_value}")
