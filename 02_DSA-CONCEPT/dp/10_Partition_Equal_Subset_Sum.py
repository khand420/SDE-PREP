def can_partition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(nums)

    # Create a DP array
    dp = [False] * (target + 1)
    dp[0] = True  # Sum of 0 can always be formed

    # Fill the DP array
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

# Example usage
nums = [1, 5, 11, 5]
result = can_partition(nums)
print(f"Can the array be partitioned into two subsets of equal sum? {result}")
