# Find the intersection of two arrays.

def intersection(nums1, nums2):
    intersection_nums = set()
    for num in nums1:
        if num in nums2:
            intersection_nums.add(num)
    return intersection_nums


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))

# Output: [9,4]
# Explanation: [4,9] is also accepted.