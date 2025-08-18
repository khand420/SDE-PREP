# Subarray sum equals k

def subarraySum(nums, k):
    cache = {0: 1}
    count = 0
    sum_ = 0

    for num in nums:
        sum_ += num
        diff = sum_ - k
        if diff in cache:
            count += cache[diff]
        cache[sum_] = cache.get(sum_, 0) + 1

    return count



nums = [1,2,4,5,6,9,]
k = 3
# nums = [1,2,3]
# k = 3
# Output: 2

print(subarraySum(nums, k))