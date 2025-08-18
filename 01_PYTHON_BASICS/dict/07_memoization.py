memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    
    # memo[n] = fib(n-1) + fib(n-2)
    # return memo[n]
    return fib(n-1) + fib(n-2)


print(fib(15))




# implement a basic cache system.**
  
# cache = {}
# def get_data(key):
#     if key in cache:
#         return cache[key]  # Return cached value
#     # Simulate data retrieval
#     data = expensive_data_retrieval(key)
#     cache[key] = data
#     return data