#User function Template for python3
# simillart to perfect sum/

class Solution:
    def findTargetSumWays(self, n, arr, target):
        # # code here 
        # summ = sum(arr)
        # x = summ+target
        # if x%2 != 0:
        #     return 0
        # else:
        #     x = x//2
            
        # dp = {}
        # arr.sort(reverse= True)
        
        # def solve(n, summ):
        #     if n ==0:
        #         if summ ==0:
        #             return 1
        #         else:
        #             return 0
            
        #     elif (summ, n) in dp:
        #         return dp[(summ, n)]
                
        #     else:
        #         item = arr[n-1]
        #         if item <= summ:
        #             c1 = solve(n-1, summ-item)
        #             c2 = solve(n-1, summ)
        #             c = c1+c2
        #         elif summ == 0:
        #             c = 1
        #         else:
        #             c = 0
                
        #         dp[(summ, n)] = c
        #         return c
            
        # return solve(n, x)
                
                
            


        # tabulation
                # code here 
        summ = sum(arr)
        x = summ + target

        if x < 0 or x % 2 != 0 or abs(target) > summ:
            return 0
        x = x // 2

        dp = [[0] * (x + 1) for _ in range(n)]

        for i in range(n):
            for j in range(x + 1):
                item = arr[i]  # ✅ Corrected index

                if i == 0:
                    if j == 0:
                        if item == 0:
                            dp[i][j] = 2  # ✅ Two ways: +0 and -0
                        else:
                            dp[i][j] = 1  # Only way: exclude it
                    elif item == j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0  # ✅ Added this to handle the "else" case
                else:
                    if item <= j:
                        dp[i][j] = dp[i - 1][j - item] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

        return dp[n - 1][x]
        
       



sol = Solution()
n = 5
arr = [1, 1, 1, 1, 1]
target = 3
print(sol.findTargetSumWays(n, arr, target))  # Output: 5