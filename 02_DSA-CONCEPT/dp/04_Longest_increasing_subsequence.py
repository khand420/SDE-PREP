def lis_recursive(arr, n, prev_index):
    if n == 0:
        return 0

    # Exclude the current element
    exclude = lis_recursive(arr, n - 1, prev_index)

    # Include the current element if it's greater than the last included element
    include = 0
    if prev_index == -1 or arr[n - 1] > arr[prev_index]:
        include = 1 + lis_recursive(arr, n - 1, n - 1)

    return max(include, exclude)

def get_lis_recursive(arr):
    return lis_recursive(arr, len(arr), -1)



def lis_dp(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Create an array to store the length of LIS at each index
    dp = [1] * n
    
    # Fill the DP table
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# output
# Length of LIS (DP): 6
# LIS (DP): [10, 22, 33, 50, 60, 80]

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

# Using Recursive Approach
length_recursive = get_lis_recursive(arr)
print("Length of LIS (Recursive):", length_recursive)

# Using Dynamic Programming Approach
length_dp = lis_dp(arr)
print("Length of LIS (DP):", length_dp)
