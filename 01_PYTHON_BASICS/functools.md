The `functools` module in Python provides higher-order functions that act on or return other functions. It includes tools for functional programming, such as decorators and utilities for working with callable objects.

### Common Functions in `functools`

1. **`functools.reduce()`**:
   - Applies a rolling computation to sequential pairs of values in a list.
   ```python
   from functools import reduce

   # Example: Calculate the product of a list of numbers
   numbers = [1, 2, 3, 4]
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # Output: 24
   ```

2. **`functools.partial()`**:
   - Creates a new function with some arguments of the original function fixed.
   ```python
   from functools import partial

   def multiply(x, y):
       return x * y

   double = partial(multiply, 2)  # Fix x=2
   print(double(5))  # Output: 10
   ```

3. **`functools.lru_cache()`**:
   - Caches the results of a function to speed up subsequent calls with the same arguments.
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)

   print(fibonacci(10))  # Output: 55
   ```

4. **`functools.wraps()`**:
   - A decorator that helps preserve the metadata of the original function when creating a wrapper function.
   ```python
   from functools import wraps

   def my_decorator(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           print("Something is happening before the function is called.")
           return func(*args, **kwargs)
       return wrapper

   @my_decorator
   def say_hello():
       return "Hello!"

   print(say_hello.__name__)  # Output: say_hello
   ```

### Example Usage
Here’s how you could use `functools` in a practical scenario:

```python
from functools import reduce, lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

numbers = [1, 2, 3, 4, 5]
sum_of_factorials = reduce(lambda x, y: x + factorial(y), numbers)
print(sum_of_factorials)  # Output: 153
```

Would you like to explore any specific function in more detail?