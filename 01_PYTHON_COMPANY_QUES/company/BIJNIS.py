def fib(num):
    if num <2 :
        return num 
    else:
        return fib(num-2) + fib(num-1) 


# print(fib(20))



for i in range(10):
    print(fib(i), end= " ")




# def fibonacci(n):
#     a = 0
#     b = 1
#     while b < n:
#         print(b, end= " ")
#         a, b = b, a + b

# fibonacci(10)


# a = 1
# for i in range(10):
#     print(a, end= " ")
#     i, a = a, a+i
