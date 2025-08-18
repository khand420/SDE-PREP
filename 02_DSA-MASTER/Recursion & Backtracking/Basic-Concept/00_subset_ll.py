def subsetsWithDup(nums, ans, i, result):
    if i == len(nums):
        result.append(ans[:])
        return  # Ensure to return after appending to result

    # Include the current number
    ans.append(nums[i])
    subsetsWithDup(nums, ans, i + 1, result)
    ans.pop()  # Backtrack

    # Exclude the current number
    indx = i + 1  # Change this line to correct the index
    while indx < len(nums) and nums[indx] == nums[indx - 1]:
        indx += 1 

    subsetsWithDup(nums, ans, indx, result)

nums = [1, 2, 2]
ans = []
i = 0
result = []
subsetsWithDup(nums, ans, i, result)
print(result)  # Print the result after the function call




# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         subset = []
#         nums.sort()

#         def create_subset(i):
#             if i == len(nums):
#                 res.append(subset[:])
#                 return 

#             subset.append(nums[i])
#             create_subset(i+1)
#             subset.pop()

#             while i + 1 < len(nums) and nums[i] == nums[i+1]:
#                 i+=1

#             create_subset(i+1)

#         create_subset(0)
#         return res


# nums = [1,2,2]
# obj = Solution()
# obj.subsetsWithDup(nums) 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
