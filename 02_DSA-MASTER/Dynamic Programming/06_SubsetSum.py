class Solution:
    # def isSubsetSum(self, arr, target_sum):
    #     N = len(arr)
        
    #     # Memoization dictionary to store previously computed results
    #     dp = {}

    #     # Helper function to solve using recursion with memoization
    #     def solve(n, sum):
    #         # Base cases
    #         if sum == 0:
    #             return True  # Target sum of 0 is always achievable with an empty subset
    #         if n == 0:
    #             return False  # No items left and sum is not 0, return False

    #         # Check if result is already computed (memoization)
    #         if (n, sum) in dp:
    #             return dp[(n, sum)]
            
    #         # Current item weight
    #         item = arr[n - 1]

    #         # If current item can be included in the subset
    #         if item <= sum:
    #             include_item = solve(n - 1, sum - item)  # Include item
    #             exclude_item = solve(n - 1, sum)        # Exclude item
    #             result = include_item or exclude_item
    #         else:
    #             # If current item can't be included, exclude it
    #             result = solve(n - 1, sum)

    #         # Memoize the result
    #         dp[(n, sum)] = result
    #         return result
        
    #     # Start the recursion with all items and the full capacity (target_sum)
    #     return solve(N, target_sum)


        def isSubsetSum(self, arr, target_sum):
            N = len(arr)
            
            # Initialize the DP array
            dp = [False] * (target_sum + 1)
            dp[0] = True  # Sum of 0 is always achievable with an empty subset
            
            # Iterate over all elements in the array
            for num in arr:
                # Update the DP array in reverse to prevent overwriting values in the same iteration
                for j in range(target_sum, num - 1, -1):
                    dp[j] = dp[j] or dp[j - num]
            
            # The answer is whether we can achieve the target sum
            return dp[target_sum]


# Driver code
if __name__ == "__main__":
    ob = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    print(ob.isSubsetSum(arr, target))  # Output: True
