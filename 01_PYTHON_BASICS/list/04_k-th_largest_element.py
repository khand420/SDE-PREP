import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums, k))  # Output: 5