def merge(nums1, m, nums2, n):
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()
    return nums1


nums1 = [1,2,3,0,0,0]
m = 3 #len(nums1)
nums2 = [2,5,6]
n = 3 #len(nums2)
# Output: [1,2,2,3,5,6]
print(merge(nums1, m, nums2, n))

