
def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # maxx = nums[0]
    # inx = 0
    # for i in range(len(nums)):
    #     if nums[i] > maxx:
    #         maxx = nums[i]
    #         inx = i
    # return inx    


    left, right = 0, len(nums) - 1
        
    while left < right:
        mid = (left + right) // 2
        # Compare mid with its next element
        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Move to the right side
        else:
            right = mid  # Move to the left side
            
    return left  # left is now the peak index


nums = [1,2,1,3,5,6,4]
# Output: 5
print(findPeakElement(nums))

    