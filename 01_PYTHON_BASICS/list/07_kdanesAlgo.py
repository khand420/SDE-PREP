def max_subarray_sum(nums):

    m= c  = nums[0]
    for i in nums[1:]:
        c   = max(i,c+i)
        m  = max(c, m)
    return m    

    # max_sum = current_sum = nums[0]
    # for num in nums[1:]:
    #     current_sum = max(num, current_sum + num)
    #     max_sum = max(max_sum, current_sum)
    # return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6