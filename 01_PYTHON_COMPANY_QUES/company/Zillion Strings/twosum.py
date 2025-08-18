import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the duration
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # Return the result of the function
    return wrapper

# Example usage
@time_calculator
def two_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))