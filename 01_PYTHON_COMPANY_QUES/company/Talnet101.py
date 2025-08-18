# iven an integer array nums that may contain duplicates, return all possible
# subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


# select user.name user.id from user join project on user.id = porject.i



# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1



def subsetsWithDup(nums):
    result = []
    nums.sort()  # Sort to handle duplicates
    def backtrack(start, path):
        result.append(path)  # Add the current subset
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            backtrack(i + 1, path + [nums[i]])  # Include nums[i] in the subset

    backtrack(0, [])
    return result

# Example usage
nums = [1, 2, 2]
output = subsetsWithDup(nums)
print(output)
