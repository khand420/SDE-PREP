def findMedianSortedArrays(nums1,nums2):

    merged = nums1+nums2
    n = len(merged)
    merged.sort()

    if n  % 2 != 0:
        return merged[n//2]
    else:
        return (merged[n//2] + merged[(n//2)-1] ) / 2.0





nums1 = [1,2]
nums2 = [3]

print(findMedianSortedArrays(nums1, nums2))





# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 