class Solution:
    def lis(self, arr):
        # code here
        n = len(arr)
        

        dp = [1] * n  # Initialize all LIS values as 1
        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


        # dp = {}
        # # arr.sort(reverse = True)
        # def solve(arr, n, li):
        #     if n == 0:
        #       return 0
        #     elif (n,li) in dp:
        #         return dp[(n,li)]
        #     else:
        #         if li == -1 or arr[n-1] < arr[li]:
        #             c1 = 1+solve(arr, n-1, n-1)
        #             c2 = solve(arr, n-1, li)
        #             c = max(c1, c2)
        #         else:
        #             c = solve(arr, n-1, li)
        #     dp[(n, li)] = c
        #     return c
        
        # return solve(arr, n, -1)



sol = Solution()
print(sol.lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # Output: 6
print(sol.lis([3, 10, 2, 1, 20]))  # Output: 3
print(sol.lis([3, 2]))  # Output: