class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        mod = 10**9 + 7

        # dp[i][j] means number of subsets from first i elements that sum up to j
        dp = [[0] * (target + 1) for _ in range(N + 1)]

        # Base case: one way to make sum 0 (empty subset)
        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            for j in range(target + 1):
                if arr[i - 1] <= j:
                    # Include or exclude the current item
                    dp[i][j] = (dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]) % mod
                else:
                    # Can't include current item
                    dp[i][j] = dp[i - 1][j]

        return dp[N][target]



    def perfectSum(self, arr, target):
        mod = 10**9 + 7
        n = len(arr)

        def count(i, total):
            # Base Case: If we reach the end of array
            if i == n:
                return 1 if total == 0 else 0

            # Option 1: Include current element if possible
            include = count(i + 1, total - arr[i]) if arr[i] <= total else 0

            # Option 2: Exclude current element
            exclude = count(i + 1, total)

            return (include + exclude) % mod

        return count(0, target)


sol = Solution()
print(sol.perfectSum([2, 3, 5, 6, 8, 10], 10))  # Output: 3 (for example)
print(sol.perfectSum([0, 0, 1], 1))  # Output: 4
