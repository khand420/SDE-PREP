class Solution:
    def prevLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n  # Initialize result list with -1
        stack = []

        for i in range(n): 
            while stack and stack[-1] >= arr[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(arr[i])

        return ans
    


arr = [3,1,0,8,6]
s = Solution().prevLargerElement(arr)
print(s)  # Output: [8, -1, 1, 3, -1]


