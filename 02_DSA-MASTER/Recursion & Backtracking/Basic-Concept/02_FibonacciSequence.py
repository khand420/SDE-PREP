def fib(n):
    memo={}
    if n == 0:
        return 0
    elif n == 1:
          return 1
    return fib(n-1) + fib(n-2)
    
    # if n not in memo:
    #     memo[n] = fib(n - 1) + fib(n - 2)
    # return memo[n]


print(fib(6))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...



def fib(n):
    if n == 0:
        print("fib(0) = 0")
        return 0
    elif n == 1:
        print("fib(1) = 1")
        return 1
    print(f"fib({n}) = fib({n-1}) + fib({n-2})")
    result = fib(n-1) + fib(n-2)
    print(f"fib({n}) = {result}")
    return result

print(fib(6))
