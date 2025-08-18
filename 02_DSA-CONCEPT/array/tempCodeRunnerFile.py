# Using set
def two_sum(nums, target):
    seen = set()
    for i in range(len(nums)):
        complement = target - nums[i] 
        if complement in seen:
            return [i, nums.index(complement)]
        seen.add(nums[i])
print(two_sum([1, 2, 3, 4], 5))