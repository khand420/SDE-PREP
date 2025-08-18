
# function to find the sum of contiguous subarray with maximum sum.
# def maxSubArraySum(arr):
#     #Your code here
#     N = len(arr)   
#     maxSum = arr[0]
#     curSum = 0
    
#     for i in range(N):
#         curSum = curSum+arr[i]
#         if curSum > maxSum:
#             maxSum = max(curSum,maxSum)
#         if curSum < 0:
#             curSum = 0
            
#     return maxSum        
            


# arr = [1,2, 3, -2, 5]

# print(maxSubArraySum(arr))

# For Input: 
# 1 2 3 -2 5
# Your Output: 
# 9
# Expected Output: 
# 9

def maxSubArraySum(arr):
    n = len(arr)
    max_sum = arr[0]
    cur_sum = 0

    for i in range(n):
        cur_sum = cur_sum + arr[i]

        if cur_sum > max_sum:
            max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum





arr = [1,2, 3, -2, 5]

print(maxSubArraySum(arr))