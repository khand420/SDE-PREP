def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0]*n
    stack = []

    for i,temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            popped = stack.pop()
            res[popped] = i-popped
        stack.append(i)
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

