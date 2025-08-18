def moveZeroes(nums):

    non_zero = 0  # Pointer for non-zero elements
    
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1


nums = [1,3,0,1,0,3,12]
# Output: [1,3,12,0,0]
print(moveZeroes(nums) )           