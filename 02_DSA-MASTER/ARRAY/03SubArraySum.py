# def subarraySum( nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     count = 0
#     prefix_sum = 0
#     prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
    
#     for num in nums:
#         prefix_sum += num  # Update the running prefix sum
#         if (prefix_sum - k) in prefix_sum_count:
#             count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
#         if prefix_sum in prefix_sum_count:
#             prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
#         else:
#             prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
    
#     return count

# nums = [1,2,1,3]
# k = 3

# print(subarraySum(nums, k))



def subarraySum(nums, k):
    count = 0
    p_sum = 0
    p_sum_d = {0:1}

    for num in nums:
        p_sum+=num

        count += p_sum_d.get(p_sum-k,0)
        p_sum_d[p_sum] = p_sum_d.get(p_sum,0) + 1
        # # print(p_sum-k)
       
        # if p_sum-k in p_sum_d:
        #     count+= p_sum_d[p_sum - k]
        # if p_sum in p_sum_d:
        #     p_sum_d[p_sum] +=1
        # else:
        #     p_sum_d[p_sum] =1
    return count



nums = [1,2,1,3]
k = 3

print(subarraySum(nums, k))






    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     count = 0
    #     sums = 0
    #     d = dict()
    #     d[0] = 1
        
    #     for i in range(len(nums)):
    #         sums += nums[i]
    #         count += d.get(sums-k,0)
    #         d[sums] = d.get(sums,0) + 1
        
    #     return(count)