def subsetsWithDup(nums):
    nums.sort()  # Sort the input to handle duplicates
    result =[] #set()  # Use a set to avoid duplicates
    for i in range(len(nums)):
        # for j in range(i+1, len(nums)+1):
        for j in range(0, len(nums)+1):

            # result.add(nums[i]+nums[j]) 
            # result.append(nums[i:j]) 
            if not nums[i:j] in result:
                result.append(nums[i:j]) 

    return result
# Example usage
nums = [1, 2, 2]
print(subsetsWithDup(nums))