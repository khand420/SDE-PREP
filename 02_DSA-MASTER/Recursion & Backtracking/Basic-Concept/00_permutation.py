def permutatiion(nums, indx, ans):

    if len(nums) == indx:
        ans.append(nums[:])
        return
    
    for i in range(indx,len(nums)):
        nums[indx], nums[i] = nums[i], nums[indx]
        permutatiion(nums, indx+1, ans) #indx place => ith element choice
        nums[indx], nums[i] = nums[i], nums[indx] #backtracking





nums = [1,2,3]
ans = []
indx = 0
permutatiion(nums, indx, ans)

print(ans)

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]