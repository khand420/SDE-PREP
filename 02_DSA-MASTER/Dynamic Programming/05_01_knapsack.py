class Solution:
    def knapsack(self, W, values, weights):
        # Get the number of items
        N = len(values)
        
        # Memoization dictionary to store previously computed results
        dp = {}

        # Helper function to solve using recursion with memoization
        def solve(n, cap):
            # Base case: no items left or no capacity
            if n == 0 or cap == 0:
                return 0
            
            # Check if result is already computed (memoization)
            if (n, cap) in dp:
                return dp[(n, cap)]
            
            # Current item weight and value
            weight = weights[n - 1]
            value = values[n - 1]
            
            # If current item can be included in the knapsack
            if weight <= cap:
                include_item = value + solve(n - 1, cap - weight)  # Include item
                exclude_item = solve(n - 1, cap)  # Exclude item
                result = max(include_item, exclude_item)
            else:
                # If current item can't be included, exclude it
                result = solve(n - 1, cap)
            
            # Memoize the result
            dp[(n, cap)] = result
            return result
        
        # Start the recursion with all items and the full capacity
        return solve(N, W)


# Driver code
if __name__ == "__main__":
    ob = Solution()
    capacity = 5
    values = [10, 40, 30, 50]
    weights = [5, 4, 2, 3]
    print(ob.knapsack(capacity, values, weights))




# def knapsackMemoization(W, wt, val, n, memo):
#     # Base case: no items left or no capacity left
#     if n == 0 or W == 0:
#         return 0
    
#     # If we have already solved this subproblem, return the cached result
#     if (n, W) in memo:
#         return memo[(n, W)]
    
#     # If the weight of the current item is more than the remaining capacity
#     if wt[n-1] > W:
#         memo[(n, W)] = knapsackMemoization(W, wt, val, n-1, memo)
#         return memo[(n, W)]
    
#     # Otherwise, compute the result for including or excluding the item
#     include_item = val[n-1] + knapsackMemoization(W - wt[n-1], wt, val, n-1, memo)
#     exclude_item = knapsackMemoization(W, wt, val, n-1, memo)
    
#     # Store the result in the memo dictionary and return the maximum value
#     memo[(n, W)] = max(include_item, exclude_item)
#     return memo[(n, W)]


# # W = 50
# # wt = [10, 20, 30]
# # val = [60, 100, 120]

# W =5
# val= [10, 40, 30, 50]
# wt= [5, 4, 2, 3] 

# n = len(val)
# memo = {}
# print(knapsackMemoization(W, wt, val, n, memo))
# knapsackMemoization(W, wt, val, n, memo)

# Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.



# ========================================================Bottom-up DP==============================================================================


class Solution:
    def knapsack(self, W, val, wt):
        N = len(val)
        
        # Initialize a DP table with 0 values
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        
        # Build the DP table
        for i in range(1, N + 1):  # Loop through each item
            for w in range(1, W + 1):  # Loop through each capacity
                if wt[i - 1] <= w:
                    # Item can be included, take the max of including or excluding
                    dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
                else:
                    # Item can't be included, exclude it
                    dp[i][w] = dp[i - 1][w]
        
        # The result will be in dp[N][W]
        return dp[N][W]


# Driver code
if __name__ == "__main__":
    ob = Solution()
    capacity = 5
    values = [10, 40, 30, 50]
    weights = [5, 4, 2, 3]
    print(ob.knapsack(capacity, values, weights))
