**Dynamic Programming (DP)** is a powerful algorithmic technique used to **optimize recursive problems** by **storing intermediate results**. It is especially useful for problems with **overlapping subproblems** and **optimal substructure**.

---

## 🔑 Core Concepts

| Term                        | Meaning                                               |
| --------------------------- | ----------------------------------------------------- |
| **Overlapping Subproblems** | Same problems solved multiple times (e.g., Fibonacci) |
| **Optimal Substructure**    | Problem can be solved using solutions of subproblems  |
| **Memoization**             | Top-down DP: Store results of recursive calls         |
| **Tabulation**              | Bottom-up DP: Build solution iteratively              |

---

## 🔁 1. **Memoization (Top-Down)**

You write a **recursive solution** and cache results.

### Example: Fibonacci

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## 📋 2. **Tabulation (Bottom-Up)**

You **build a table** from smaller subproblems to the final answer.

### Example: Fibonacci

```python
def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

---

## 🧱 3. Typical DP Problem Types

| Problem Type              | Examples                                   |
| ------------------------- | ------------------------------------------ |
| 1D DP                     | Fibonacci, Climbing Stairs                 |
| 2D DP                     | Knapsack, Longest Common Subsequence       |
| DP with States            | Edit Distance, Matrix Chain Multiplication |
| Subset/Partition Problems | Subset Sum, Equal Partition                |
| Greedy + DP               | Jump Game II, Minimum Path Sum             |

---

## 🎯 Steps to Solve DP Problems

1. **Identify subproblem** – What is the smallest version?
2. **Define DP state** – What parameters define your state?
3. **Recurrence relation** – How does state `i` depend on previous?
4. **Base case(s)** – What are the simplest cases?
5. **Decide memoization or tabulation**
6. **Optimize space (if needed)**

---

## 🧠 Classic Examples to Learn From:

| Problem                        | Type               |
| ------------------------------ | ------------------ |
| Climbing Stairs                | 1D DP              |
| House Robber                   | 1D DP              |
| Longest Increasing Subsequence | 1D DP              |
| Longest Common Subsequence     | 2D DP              |
| 0/1 Knapsack                   | 2D DP              |
| Coin Change                    | Unbounded Knapsack |
| Edit Distance                  | DP with States     |

---

Would you like me to walk you through one of these problems (with code and explanation)?
