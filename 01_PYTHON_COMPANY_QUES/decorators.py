# import time

# def cal_time(func):
#     def wrapper(*args, **kwargs):
#         s = time.time()
#         out = func(*args, **kwargs)
#         e = time.time()
#         print(f"func {func.__name__!r} executed in {(e-s):.4f} seconds")
#         return out    
#     return wrapper

# @cal_time
# def mul():
#     return 9 * 9

# # Call the function and print the result
# print(mul())








# def cal_time(message):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             s = time.time()
#             out = func(*args, **kwargs)
#             e = time.time()
#             print(f"{message} - func {func.__name__!r} executed in {(e-s):.4f} seconds")
#             return out
#         return wrapper
#     return decorator

# @cal_time("Calculating time")
# def mul(a, b):
#     return a * b

# # Call the function and print the result
# print(mul(9, 9))





# import time

# def cal_time(message, show_start_time):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if show_start_time:
#                 start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#                 print(f"Start time: {start_time}")
#             s = time.time()
#             out = func(*args, **kwargs)
#             e = time.time()
#             print(f"{message} - func {func.__name__!r} executed in {(e-s):.4f} seconds")
#             return out
#         return wrapper
#     return decorator

# @cal_time("Calculating time", True)
# def mul(a, b):
#     return a * b

# # Call the function and print the result
# print(mul(9, 9))

# @cal_time("Execution time for addition", False)
# def add(a, b):
#     return a + b

# # Call the function and print the result
# print(add(10, 20))



def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before the function call.")
        result = func(*args, **kwargs)
        print("Decorator 1: After the function call.")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before the function call.")
        result = func(*args, **kwargs)
        print("Decorator 2: After the function call.")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the function
say_hello("Alice")



def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
