class Solution:
    def threeSum(self, nums):
        # ans=set()
        # nums.sort()
        # n=len(nums)
        # for i in range(n-2):
        #     j=i+1
        #     k=n-1
        #     while j<k:
        #         temp=nums[i]+nums[j]+nums[k]
        #         if temp==0:
        #             ans.add((nums[i],nums[j],nums[k]))
        #             j+=1
        #         elif temp>0:
        #             k-=1
        #         else:
        #             j+=1
        # return ans
    
    
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=nums[i]+nums[j]+nums[k]
                    if temp==0:
                        ans.add((nums[i],nums[j],nums[k]))
        return ans



nums = [-1,0,1,2,-1,-4]

sum = Solution()
print(sum.threeSum(nums))
# sum.threeSum(nums)



# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.