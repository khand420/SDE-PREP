
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    start, current, end = 0, 0, len(nums)-1

    while current <=end:
        if nums[current] == 0:
            nums[start], nums[current] = nums[current], nums[start]

            start +=1
            current +=1

        elif nums[current] == 1:
            current +=1

        else:
            nums[current], nums[end] = nums[end], nums[current]    

            end-=1
    return nums            


nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

print(sortColors(nums))