class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n

        # Initialize up and down arrays
        up = down = result = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1

            result = max(result, up, down)

        return result



# dp
    # def maxTurbulenceSize(self, arr):
    #     n = len(arr)
    #     if n < 2:
    #         return n

    #     up = [1] * n
    #     down = [1] * n
    #     max_len = 1

    #     for i in range(1, n):
    #         if arr[i] > arr[i - 1]:
    #             up[i] = down[i - 1] + 1
    #             down[i] = 1
    #         elif arr[i] < arr[i - 1]:
    #             down[i] = up[i - 1] + 1
    #             up[i] = 1
    #         else:
    #             up[i] = down[i] = 1

    #         max_len = max(max_len, up[i], down[i])

    #     return max_len




sol = Solution()
print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))  # Output: 5
