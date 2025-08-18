def containsNearbyDuplicate(nums, k):
    num_set = set()

    for i in range(len(nums)):
        # If the window size exceeds k, remove the oldest element
        if i > k:
            num_set.remove(nums[i - k - 1])

        # Check if the current element is already in the set
        if nums[i] in num_set:
            return True

        # Add the current element to the set
        num_set.add(nums[i])

    return False

# Example usage
nums = [1, 2, 3, 1]
k = 3

# Function Call
result = containsNearbyDuplicate(nums, k)
print(result)  # Output: True
