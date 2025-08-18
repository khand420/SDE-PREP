Here are well-documented answers to the additional Python interview questions:

---

### 21. **What are metaclasses in Python?**

A **metaclass** in Python is a "class of a class" — it defines how classes themselves are created and behaves. While normal classes define the structure and behavior of instances, a metaclass defines how classes are instantiated and how their behavior is defined.

* **Metaclasses** are used to control class creation and can be used to enforce coding standards, modify class attributes, and more.
* By default, all classes are instances of the `type` metaclass, but you can define your own custom metaclass by inheriting from `type`.

#### Example:

```python
# A simple metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'This is an added attribute'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.added_attribute)  # Output: This is an added attribute
```

Metaclasses can be powerful but should be used carefully to avoid complexity.

---

### 22. **What is monkey patching?**

**Monkey patching** refers to modifying or extending the behavior of a module or class at runtime. It is typically used to fix bugs or add new functionality to third-party code without modifying the original source.

While it can be useful in certain situations, monkey patching can lead to maintenance challenges, as it changes code dynamically and can cause unexpected side effects.

#### Example:

```python
class MyClass:
    def say_hello(self):
        print("Hello")

# Monkey patching the say_hello method
def new_say_hello(self):
    print("Hello, world!")

MyClass.say_hello = new_say_hello

obj = MyClass()
obj.say_hello()  # Output: Hello, world!
```

---

### 23. **How does memory management work in Python (ref count, GC)?**

Python uses two primary mechanisms for memory management:

1. **Reference Counting**: Every object in Python has an associated reference count, which tracks how many references point to the object. When the reference count drops to zero, the object is deallocated.

2. **Garbage Collection (GC)**: Python uses a garbage collector (based on cyclic reference detection) to clean up objects involved in circular references (i.e., objects that refer to each other in a cycle). The `gc` module handles this process.

Python’s memory management is automatic, and you generally don’t have to worry about deallocating memory explicitly.

```python
import gc
gc.collect()  # Force garbage collection
```

---

### 24. **How would you implement an LRU (Least Recently Used) cache from scratch?**

An **LRU cache** stores a limited number of items, evicting the least recently used item when the cache exceeds its capacity.

To implement this efficiently, you can use a **hashmap** (for fast access) along with a **doubly linked list** (to maintain the order of access).

* **Doubly linked list**: The most recently used item is moved to the front, and the least recently used item is at the back.
* **Hashmap**: Allows for O(1) lookup of values.

#### Example:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Move the accessed item to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

# Example usage
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # Output: 1
lru.put(3, 3)      # Removes key 2
print(lru.get(2))  # Output: -1
```

---

### 25. **What is the difference between `@staticmethod`, `@classmethod`, and instance methods?**

* **Instance Method**: A method that operates on an instance of the class and takes `self` as its first parameter.

  ```python
  class MyClass:
      def instance_method(self):
          print("Instance method")
  ```

* **Class Method**: A method that operates on the class itself and takes `cls` as its first parameter. It is defined using the `@classmethod` decorator.

  ```python
  class MyClass:
      @classmethod
      def class_method(cls):
          print("Class method")
  ```

* **Static Method**: A method that doesn't operate on the instance or the class. It’s independent of the class and instance and is defined using the `@staticmethod` decorator.

  ```python
  class MyClass:
      @staticmethod
      def static_method():
          print("Static method")
  ```

---

### 26. **Explain closures and lexical scoping in Python.**

* **Closure**: A closure is a function object that remembers values in its enclosing lexical scope, even if the program flow has moved out of the scope.

* **Lexical Scoping**: In Python, a function’s scope is determined by where it is defined, not where it is called. This allows nested functions to access variables in their enclosing functions, which leads to closures.

#### Example:

```python
def outer_func(outer_variable):
    def inner_func(inner_variable):
        return outer_variable + inner_variable
    return inner_func

closure = outer_func(10)
print(closure(5))  # Output: 15
```

Here, `inner_func` is a closure because it remembers the `outer_variable` even after `outer_func` finishes execution.

---

### 27. **What are dataclasses in Python 3.7+?**

**Dataclasses** are a feature introduced in Python 3.7 that simplifies the creation of classes used to store data. It automatically generates special methods like `__init__`, `__repr__`, `__eq__`, and `__hash__` for you.

You use the `@dataclass` decorator to define a dataclass.

#### Example:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
print(p1)  # Output: Point(x=1, y=2)
```

Dataclasses reduce boilerplate code for classes that are primarily used to store attributes.

---

### 28. **How does Python handle async I/O (`async/await`)?**

Python handles **asynchronous I/O** using the `asyncio` library, which provides an event loop to manage tasks. With `async` and `await`, you can define asynchronous functions that run concurrently, making I/O-bound operations more efficient.

* **`async`** is used to define an asynchronous function.
* **`await`** is used to pause the execution of the function until the awaited task completes.

#### Example:

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")

async def main():
    await fetch_data()

asyncio.run(main())
```

This example demonstrates asynchronous execution, where the program can perform other tasks while waiting for `fetch_data` to complete.

---

### 29. **What are the performance differences between NumPy arrays and Python lists?**

* **Memory Efficiency**: NumPy arrays are more memory-efficient than Python lists, as they store data in contiguous blocks of memory, whereas lists store references to objects.

* **Performance**: NumPy arrays are faster for numerical operations because they are implemented in C, and operations are vectorized (i.e., they operate on entire arrays at once). Python lists, on the other hand, are slower for such operations because they require looping over elements and using individual Python operations.

#### Example:

```python
import numpy as np

# NumPy array
arr = np.array([1, 2, 3])
arr = arr * 2  # Element-wise operation, very fast

# Python list
lst = [1, 2, 3]
lst = [x * 2 for x in lst]  # List comprehension, slower than NumPy
```

NumPy is ideal for large numerical datasets and mathematical operations.

---

### 30. **What are some Python 3.x features that didn’t exist in Python 2.x?**

Here are a few key features introduced in Python 3.x that did not exist in Python 2.x:

1. **`print()` as a function**: In Python 2.x, `print` was a statement. In Python 3.x, `print()` is a function.

   ```python
   print("Hello, world!")
   ```

2. **Unicode strings by default**: In Python 3, strings are Unicode by default, whereas in Python 2, strings were ASCII by default.

3. **`input()` function**: In Python 2.x, `input()` evaluated the input as code. Python 3.x’s `input()` always returns a
