# def productExceptSelf(arr):
#     n = len(arr)
#     narr= [1] *n
#     for i in range(n):
#         for j in range(n):
#             if i !=j:
#               narr[i] *= arr[j]
#     return narr
# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 2]
#     res = productExceptSelf(arr)
#     print(" ".join(map(str, res)))



def productExceptSelf(nums):
    output = [1] * len(nums)
    
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]
    # output = [1,-1,-1,0,0]
    #output = [1,10,30,150,900]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output 
    
arr =  [10, 3, 5, 6, 2] #[-1,1,0,-3,3] 
# output = [180, 600, 360, 300, 900]
print(productExceptSelf(arr))


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

arr = [10, 3, 5, 6, 2]
# [180, 600, 360, 300, 900]


def mul(arr):

    n = len(arr)
    output  = [1] * n
    # print('-------------',output)
    left = 1
    for i in range(n):
        output[i] *=  left 
        left *= arr[i]
        # print('-------------',output, left)
    right = 1
    for i in range(n-1, -1, -1):
        output[i]*= right 
        right*=arr[i]
        
    return output


arr = [-1,1,0,-3,3]

print(mul(arr))