# # Using set
# def two_sum(nums, target):
#     seen = set()
#     for i in range(len(nums)):
#         complement = target - nums[i] 
#         if complement in seen:
#             return [i, nums.index(complement)]
#         seen.add(nums[i])
# print(two_sum([1, 2, 3, 4], 5))



# Using dict
def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        complement = target - nums[i] 
        if complement in d:
            return [i, d[complement] ]
        d[nums[i]] = i
print(two_sum([1, 2, 3, 4], 5))