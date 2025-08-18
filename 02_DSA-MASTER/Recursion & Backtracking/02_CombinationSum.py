def combinationSum(arr,indx, target, ans, combin):
    
    if indx == len(arr) or target < 0:
        return
    
    if target == 0:
        # ans.append(combin[:])
        ans.add(tuple(combin[:]))
        return
    
    combin.append(arr[indx])

    # single inculusion
    combinationSum(arr,indx+1, target - arr[indx], ans, combin)
    
     # multiple inculusion
    combinationSum(arr,indx, target - arr[indx], ans, combin)
   
    combin.pop()
  
    #Execulusion
    combinationSum(arr,indx+1 , target, ans, combin)


arr = [2,3,5]  #[2,3,6,7]
target =  8 #7
indx = 0
ans = []
ans = set()
combin = []
combinationSum(arr,indx, target, ans, combin)
print(ans)
unique_combinations = [list(comb) for comb in ans]
print(unique_combinations)


# def combinationSum(candidates, target):
        
#     res = []

#     def make_combination(idx, comb, total):
#         if total == target:
#             res.append(comb[:])
#             return
        
#         if total > target or idx >= len(candidates):
#             return
        
#         comb.append(candidates[idx])
#         make_combination(idx, comb, total + candidates[idx])
#         comb.pop()
#         make_combination(idx+1, comb, total)

#         return res

#     return make_combination(0, [], 0)


# candidates = [2,3,6,7]
# target = 7
# print(combinationSum(candidates, target))




# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40