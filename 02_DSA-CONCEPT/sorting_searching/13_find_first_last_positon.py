
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    out = [] 
    for i in range(len(nums)):
        if nums[i] == target:
            out.append(i)
    if len(out) >= 2:
        return [out[0], out[-1]]
    elif len(out) == 1:
        return [out[0], out[0]]
    return [-1,-1]        


nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]   

print(searchRange(nums, target))