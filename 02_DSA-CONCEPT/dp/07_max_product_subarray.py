def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        max_product = max(max_product, current_max)

    return max_product

# Example usage
nums = [2, 3, -2, 4]
result = max_product_subarray(nums)
print(f"The maximum product subarray is: {result}")
