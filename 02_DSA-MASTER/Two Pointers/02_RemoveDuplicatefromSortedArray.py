class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[:] = sorted(set(nums))
        # return len(nums)
        # s = set(nums)
        # print('000000000000000',s)
        # return list(s)

        # newArr = [] * len(nums)
        # seen = set()
        
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        # print(list(seen))
        # return list(seen)


        # if not nums:
        #     return 0
    
        # j = 0
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums[i]
        
        # return j + 1

        
        if not nums:
            return 0
        j = 0

        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
        return j+1

nums = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))





# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 



nums = [1, 2, 3, 4]
copy_of_nums = nums[:]  # Creates a shallow copy
print("Creates a shallow copy" ,copy_of_nums)      # Output: [1, 2, 3, 4]

# Modifying the original list
nums[0] = 10
print ("Modifying the original list", nums)              # Output: [10, 2, 3, 4]
print("remains unchanged", copy_of_nums)      # Output: [1, 2, 3, 4] (remains unchanged)
