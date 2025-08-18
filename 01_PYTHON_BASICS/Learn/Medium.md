Here are well-documented answers to your listed Python interview questions:

---

### 11. **Explain Python’s object-oriented features.**

Python supports **object-oriented programming (OOP)**, which is a programming paradigm based on the concept of objects. Key OOP features in Python:

1. **Classes**: Python allows you to define classes to structure your code around objects. A class is a blueprint for creating objects (instances).

   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model
   ```

2. **Objects**: Objects are instances of a class that contain both data (attributes) and methods (functions).

   ```python
   my_car = Car("Toyota", "Corolla")
   ```

3. **Encapsulation**: The concept of bundling the data (attributes) and methods (functions) that operate on the data within a class. This can also involve hiding private details by using access specifiers like `_` (protected) and `__` (private).

   ```python
   class BankAccount:
       def __init__(self, balance):
           self.__balance = balance  # Private attribute

       def deposit(self, amount):
           self.__balance += amount
   ```

4. **Inheritance**: Python supports inheritance, allowing one class (child class) to inherit methods and properties from another (parent class).

   ```python
   class ElectricCar(Car):
       def __init__(self, make, model, battery_size):
           super().__init__(make, model)
           self.battery_size = battery_size
   ```

5. **Polymorphism**: Different classes can have methods with the same name but different implementations, or a method can behave differently based on the object type.

   ```python
   class Dog:
       def speak(self):
           print("Woof")

   class Cat:
       def speak(self):
           print("Meow")

   def animal_sound(animal):
       animal.speak()  # Polymorphism in action
   ```

6. **Abstraction**: Python allows you to hide complex implementation details and expose only essential features. This is typically done using abstract classes and methods (via `abc` module).

---

### 12. **What is the difference between a class method, static method, and instance method?**

1. **Instance Method**: A regular method that takes `self` as its first argument. It operates on instance attributes and is bound to an instance of the class.

   ```python
   class MyClass:
       def instance_method(self):
           print("This is an instance method")
   ```

2. **Class Method**: A method that takes `cls` as its first argument, which refers to the class itself, not an instance. It’s defined with the `@classmethod` decorator.

   ```python
   class MyClass:
       @classmethod
       def class_method(cls):
           print("This is a class method")
   ```

3. **Static Method**: A method that doesn't take `self` or `cls` as its first argument. It doesn't access or modify class or instance state. Defined with the `@staticmethod` decorator.

   ```python
   class MyClass:
       @staticmethod
       def static_method():
           print("This is a static method")
   ```

---

### 13. **What is the Global Interpreter Lock (GIL)?**

The **Global Interpreter Lock (GIL)** is a mutex (lock) in CPython (the default Python implementation) that allows only **one thread to execute Python bytecode at a time**. While this simplifies memory management, it can be a bottleneck for CPU-bound tasks in multi-threaded programs, as threads have to wait for the GIL to be released.

For **I/O-bound tasks** (e.g., file operations, web requests), Python can still use multiple threads efficiently because threads spend most of their time waiting for I/O.

To bypass the GIL limitation in CPU-bound tasks, you can use **multiprocessing** instead of **multithreading**.

---

### 14. **How is exception handling done in Python?**

Python uses the `try`, `except`, `else`, and `finally` blocks for exception handling:

1. **`try`**: Code that may raise an exception is put inside the `try` block.
2. **`except`**: Block that handles exceptions raised by the `try` block.
3. **`else`**: Optional block that runs if no exception was raised in the `try` block.
4. **`finally`**: Block that always executes, regardless of whether an exception was raised or not.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
else:
    print("No error occurred")
finally:
    print("This will always run")
```

---

### 15. **What are decorators in Python? Give an example.**

A **decorator** is a function that wraps another function to modify its behavior. Decorators are commonly used for logging, access control, memoization, and more.

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello, world!")

say_hello()
```

Output:

```
Before function call
Hello, world!
After function call
```

---

### 16. **What is a generator in Python? How does `yield` work?**

A **generator** is a function that returns an iterator using the `yield` keyword. When `yield` is used, the function’s state is saved, and it can continue from where it left off when the next value is requested.

Generators are memory-efficient because they yield items one by one, instead of generating all items at once.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

gen = count_up_to(5)
for num in gen:
    print(num)
```

Output:

```
1
2
3
4
5
```

---

### 17. **What is the difference between `deepcopy()` and `copy()`?**

* **`copy()`** creates a **shallow copy** of an object. If the object contains references to other objects, it does not create copies of the nested objects. It just copies references to them.

* **`deepcopy()`** creates a **deep copy** of an object, including copies of all nested objects. Thus, it avoids the issue of references to the same object.

```python
import copy
original = [1, [2, 3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[1][0] = 9
print(original)  # [1, [9, 3]]
print(shallow)   # [1, [9, 3]]
print(deep)       # [1, [2, 3]]
```

---

### 18. **How does Python handle multithreading and multiprocessing?**

* **Multithreading**: Python’s `threading` module allows multiple threads within a single process. However, due to the GIL, threads cannot run Python bytecode simultaneously. This makes multithreading suitable for **I/O-bound tasks** but less effective for **CPU-bound tasks**.

* **Multiprocessing**: Python’s `multiprocessing` module allows the creation of multiple processes, each with its own Python interpreter and GIL. This is better suited for **CPU-bound tasks** as processes run concurrently on multiple CPUs.

---

### 19. **What is the use of `with` statement/context manager?**

The `with` statement simplifies exception handling and resource management (like files or network connections) by automatically acquiring and releasing resources. It ensures that resources are properly cleaned up when done, even if an exception occurs.

```python
with open('file.txt', 'r') as file:
    content = file.read()
# No need to explicitly close the file, it's automatically closed when the block ends
```

The `with` statement uses a **context manager**, which defines `__enter__()` and `__exit__()` methods to handle resource setup and cleanup.

---

### 20. **How do you implement a custom iterator in Python?**

To create a custom iterator, you need to define a class with `__iter__()` and `__next__()` methods:

* `__iter__()` returns the iterator object itself.
* `__next__()` returns the next value and raises `StopIteration` when the iteration is finished.

```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('giraffe')
for char in rev:
    print(char)
```

Output:

```
e
f
a
r
i
g
```

---

These answers provide a concise yet detailed understanding of the topics you’ve listed. Let me know if you need further clarification or examples!
