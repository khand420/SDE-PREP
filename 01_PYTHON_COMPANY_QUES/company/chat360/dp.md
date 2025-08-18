To solve this problem, we can use dynamic programming to find the minimum cost to cover all the travel days using the given passes. The idea is to keep track of the minimum cost required to cover travel up to each day in the input list.

Here's how we can approach the solution:

1. Create an array `dp` where `dp[i]` represents the minimum cost to travel up to the ith day.
2. Initialize a set `days_set` to store the days on which travel is required for quick lookup.
3. Iterate through each day from 1 to the last day in the `days` list.
4. For each day:
   - If it's not a travel day, the cost remains the same as the previous day.
   - If it's a travel day, calculate the cost for using a 1-day, 7-day, or 30-day pass and update the dp array with the minimum cost.

Let's implement this approach in Python:

```python
def min_cost_travel(days, costs):
    # Initialize a set with the travel days for quick lookup
    days_set = set(days)
    # Maximum day in the travel days list
    max_day = days[-1]
    
    # Create a dp array with size (max_day + 1) and initialize all values to 0
    dp = [0] * (max_day + 1)
    
    for i in range(1, max_day + 1):
        if i not in days_set:
            # If i is not a travel day, the cost is the same as the previous day
            dp[i] = dp[i - 1]
        else:
            # Calculate the cost using 1-day, 7-day, and 30-day pass
            cost1 = dp[i - 1] + costs[0]  # 1-day pass
            cost7 = dp[i - 7] + costs[1] if i >= 7 else costs[1]  # 7-day pass
            cost30 = dp[i - 30] + costs[2] if i >= 30 else costs[2]  # 30-day pass
            
            # Update dp[i] with the minimum cost
            dp[i] = min(cost1, cost7, cost30)
    
    return dp[max_day]

# Test case
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(min_cost_travel(days, costs))  # Output: 11
```

### Explanation:
1. We initialize the `days_set` with the travel days for quick lookup and the `dp` array with all values set to 0.
2. We iterate from day 1 to the maximum travel day.
3. If the current day is not a travel day, we set `dp[i]` to `dp[i-1]`.
4. If the current day is a travel day, we calculate the cost of using a 1-day, 7-day, or 30-day pass and update `dp[i]` with the minimum cost.
5. Finally, the value at `dp[max_day]` gives the minimum cost to travel on all required days.

This approach ensures that we find the minimum cost to cover all the travel days using the given passes.