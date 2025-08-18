def find_median(nums):

    nums.sort()
    n = len(nums)
    mid = n//2

    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid ])/2
    else:
        return nums[mid] 



    # nums.sort()
    # n = len(nums)
    # mid = n // 2
    # if n % 2 == 0:
    #     return (nums[mid - 1] + nums[mid]) / 2
    # else:
    #     return nums[mid]

# Example
nums = [3, 1, 2, 5, 4]
print(find_median(nums))  # Output: 3