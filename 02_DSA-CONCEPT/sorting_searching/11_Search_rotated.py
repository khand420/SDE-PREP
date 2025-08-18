def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # return -1     

    if target not in nums:
        return -1
    return nums.index(target)       

nums = [4,5,6,7,0,1,2]
target = 0

print(search( nums, target))