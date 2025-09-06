class Solution(object):

    def  maxProduct(self, arr):

        n = len(arr)
        mx = arr[0]
        mn = arr[0]
        ans = arr[0]
        for i in range(1, n):
            el = arr[i]
            c1 = el
            c2 = el * mn
            c3 = el * mx
            mn = min(c1,c2,c3)
            mx = max(c1,c2,c3)
            ans = max(ans, mx)
        return ans

    # def maxProduct(self, nums):
    #     n = len(nums)
    #     if n == 0:
    #         return 0

    #     max_so_far = nums[0]
    #     min_so_far = nums[0]
    #     result = nums[0]

    #     for i in range(1, n):
    #         if nums[i] < 0:
    #             max_so_far, min_so_far = min_so_far, max_so_far

    #         max_so_far = max(nums[i], max_so_far * nums[i])
    #         min_so_far = min(nums[i], min_so_far * nums[i])

    #         result = max(result, max_so_far)

    #     return result


sol = Solution()
print(sol.maxProduct([2,3,-2,4]))  # Output: 6
print(sol.maxProduct([-2,0,-1]))  # Output: 0
print(sol.maxProduct([-2,3,-4]))  # Output: 24
print(sol.maxProduct([-2]))  # Output: -2
print(sol.maxProduct([-2,-3,-4]))  # Output: 12

      