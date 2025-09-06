
## 🔁 1. **Memoization (Top-Down)**
# You write a **recursive solution** and cache results.

# def fib(n, memo={}):
#     if n <= 1:
#         return n
#     if n not in memo:
#         memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]



## 📋 2. **Tabulation (Bottom-Up)**
# You **build a table** from smaller subproblems to the final answer.

def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

# Example usage
if __name__ == "__main__":      
    n = 10  # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is: {fib(n)}")