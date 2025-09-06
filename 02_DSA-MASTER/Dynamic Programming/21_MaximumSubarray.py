# Kadane's Algorithm | Maximum Subarray 


class Solution(object):
    # 1DP
    # def maxSubArray(self, arr):
    #     n = len(arr)
    #     dp = [0]*n

    #     dp[0] = arr[0]
    #     for i in range(1, n):
    #         c1 = arr[i]
    #         c2 = dp[i-1]+arr[i]
    #         dp[i] = max(c1, c2)

    #     return max(dp)

    # without DP array


    def maxSubArray(self, arr):
        n = len(arr)
        temp = arr[0]
        mx = arr[0]
        for i in range(1, n):
            c1 = arr[i]
            c2 = temp+arr[i]
            temp = max(c1,c2)
            mx = max(mx, temp)
        return mx


    # def maxSubArray(self, arr):
    #     n = len(arr)
    #     max_sum = arr[0]
    #     curr_sum = arr[0]

    #     for i in range(1, n):
    #         curr_sum = max(arr[i], curr_sum + arr[i])
    #         max_sum = max(max_sum, curr_sum)

    #     return max_sum


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23  