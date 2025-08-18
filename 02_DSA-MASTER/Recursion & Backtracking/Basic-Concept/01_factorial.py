def factorial(n):
    if n == 0:
        return 1
    # print(n)
    return n * factorial(n-1)

print(factorial(5))