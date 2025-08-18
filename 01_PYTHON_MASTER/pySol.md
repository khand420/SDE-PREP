Sure! I'll provide concise answers to each of the theoretical and practical Python interview questions listed. 

### Theoretical Python Questions

1. **Core Python Concepts:**
   - **Key Features:** Easy syntax, dynamic typing, extensive libraries, and strong community support.
   - **Python 2.x vs 3.x:** Python 3.x has improved Unicode support, print as a function, and various library updates. Python 2.x is no longer supported.
   - **Built-in Data Types:** int, float, str, list, tuple, set, dict, bool.
   - **Garbage Collection:** Python uses reference counting and cyclic garbage collection to manage memory.
   - **Memory Management:** Managed by Python's memory manager, which handles allocation and deallocation.

2. **Data Structures:**
   - **List vs Tuple vs Set vs Dictionary:** 
     - List: Ordered, mutable, allows duplicates.
     - Tuple: Ordered, immutable, allows duplicates.
     - Set: Unordered, mutable, no duplicates.
     - Dictionary: Unordered, mutable, key-value pairs.
   - **Stacks and Queues:** Use lists for stacks (append/pop) and collections.deque for queues (appendleft/pop).
   - **List Comprehensions:** A concise way to create lists. Example: `[x**2 for x in range(10)]`.
   - **Slicing:** Extracts a portion of a list, e.g., `my_list[1:3]`.
   - **Defaultdict:** A subclass of dict that provides default values for missing keys.

3. **Functions:**
   - **`*args` and `**kwargs`:** Allow passing variable numbers of arguments. Example:
     ```python
     def func(*args, **kwargs):
         print(args, kwargs)
     ```
   - **Lambda Functions:** Anonymous functions defined with `lambda`. Example: `square = lambda x: x**2`.
   - **Decorators:** Functions that modify other functions. Example:
     ```python
     def my_decorator(func):
         def wrapper():
             print("Something before")
             func()
             print("Something after")
         return wrapper
     ```
   - **Generator Functions:** Use `yield` to return values one at a time. They are memory efficient.
   - **First-Class Functions:** Functions that can be passed as arguments, returned from other functions, and assigned to variables.

4. **Object-Oriented Programming (OOP):**
   - **Class vs Object:** A class is a blueprint; an object is an instance of a class.
   - **Inheritance & Polymorphism:** Inheritance allows classes to inherit attributes and methods from other classes. Polymorphism allows methods to do different things based on the object.
   - **`__init__` and `__str__`:** `__init__` initializes an object; `__str__` defines the string representation.
   - **Metaclasses:** Classes of classes that define how classes behave.
   - **Abstract Class:** Use the `abc` module to create abstract classes.

5. **Error Handling:**
   - **Handling Exceptions:** Use `try`, `except` to catch exceptions. Example:
     ```python
     try:
         # code
     except Exception as e:
         print(e)
     ```
   - **Custom Exceptions:** Define a new exception class for specific error handling.
   - **`try`, `except`, `finally`, `else`:** `finally` always runs, `else` runs if no exception occurs.

6. **Modules and Packages:**
   - **Module vs Package:** A module is a single file; a package is a directory of modules.
   - **Importing Modules:** Use `import module_name` or `from module_name import function_name`.
   - **`__init__.py`:** Indicates that a directory should be treated as a package.

7. **Concurrency and Parallelism:**
   - **GIL:** Global Interpreter Lock prevents multiple native threads from executing Python bytecodes simultaneously, affecting multi-threading.
   - **Threading vs Multiprocessing vs Asyncio:** 
     - Threading is for I/O-bound tasks.
     - Multiprocessing is for CPU-bound tasks.
     - Asyncio is for managing I/O-bound tasks using an event loop.
   - **Thread-Safe Counter:** Use `threading.Lock()` to ensure thread safety.

8. **File Handling:**
   - **Reading/Writing Files:** Use `open()`, `read()`, `write()`. Example:
     ```python
     with open('file.txt', 'r') as f:
         data = f.read()
     ```
   - **Context Managers:** Automatically manage resources. The `with` statement ensures proper acquisition and release.
   - **Binary Files:** Use `'rb'` or `'wb'` mode in `open()`.

9. **Python’s Standard Library:**
   - **`collections` Module:** Provides specialized container datatypes like `Counter`, `deque`, and `defaultdict`.
   - **`itertools` Module:** Offers functions that create iterators for efficient looping.
   - **`functools` Module:** Provides higher-order functions for function manipulation (e.g., `lru_cache`).

10. **Testing:**
    - **Unit Tests:** Use `unittest` or `pytest` to write tests.
    - **`assert`:** Used to verify conditions in tests. Example: `assert func() == expected_value`.
    - **Mocking:** Replace parts of your system under test and make assertions on how they have been used.

### Practical Python Coding Questions

1. **Recursion:**
   - **Factorial:**
     ```python
     def factorial(n):
         return 1 if n == 0 else n * factorial(n - 1)
     ```
   - **Fibonacci:**
     ```python
     def fibonacci(n):
         return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
     ```
   - **Tower of Hanoi:**
     ```python
     def tower_of_hanoi(n, source, target, auxiliary):
         if n == 1:
             print(f"Move disk 1 from {source} to {target}")
             return
         tower_of_hanoi(n - 1, source, auxiliary, target)
         print(f"Move disk {n} from {source} to {target}")
         tower_of_hanoi(n - 1, auxiliary, target, source)
     ```

2. **String Manipulation:**
   - **Palindrome Check:**
     ```python
     def is_palindrome(s):
         return s == s[::-1]
     ```
   - **Longest Common Prefix:**
     ```python
     def longest_common_prefix(strs):
         if not strs:
             return ""
         prefix = strs[0]
         for s in strs[1:]:
             while not s.startswith(prefix):
                 prefix = prefix[:-1]
         return prefix
     ```
   - **Reverse Words:**
     ```python
     def reverse_words(sentence):
         return ' '.join(sentence.split()[::-1])
     ```

3. **Data Structures:**
   - **Remove Duplicates:**
     ```python
     def remove_duplicates(lst):
         return list(set(lst))
     ```
   - **Anagram Check:**
     ```python
     def are_anagrams(str1, str2):
         return sorted(str1) == sorted(str2)
     ```
   - **Flatten Nested List:**
     ```python
     def flatten(lst):
         flat_list = []
         for item in lst:
             if isinstance(item, list):
                 flat_list.extend(flatten(item))
             else:
                 flat_list.append(item)
         return flat_list
     ```

4. **Algorithms:**
   - **Binary Search:**
     ```python
     def binary_search(arr, target):
         low, high = 0, len(arr) - 1
         while low <= high:
             mid = (low + high) // 2
             if arr[mid] < target:
                 low = mid + 1
             elif arr[mid] > target:
                 high = mid - 1
             else:
                 return mid
         return -1
     ```
   - **Quicksort:**
     ```python
     def quicksort(arr):
         if len(arr) <= 1:
             return arr
         pivot = arr[len(arr) // 2]
         left = [x for x in arr if x < pivot]
         middle = [x for x in arr if x == pivot]
         right = [x for x in arr if x > pivot]
         return quicksort(left) + middle + quicksort(right)
     ```
   - **Merge Two Sorted Lists:**
     ```python
     def merge_sorted_lists(l1, l2):
         merged = []
         i, j = 0, 0
         while i < len(l1) and j < len(l2):
             if l1[i] < l2[j]:
                 merged.append(l1[i])
                 i += 1
             else:
                 merged.append(l2[j])
                 j += 1
         merged.extend(l1[i:])
         merged.extend(l2[j:])
         return merged
     ```

5. **OOP Concepts:**
   - **BankAccount Class:**
     ```python
     class BankAccount:
         def __init__(self, balance=0):
             self.balance = balance
         
         def deposit(self, amount):
             self.balance += amount
         
         def withdraw(self, amount):
             if amount <= self.balance:
                 self.balance -= amount
             else:
                 print("Insufficient funds")
         
         def check_balance(self):
             return self.balance
     ```
   - **Shape Class:**
     ```python
     class Shape:
         def area(self):
             raise NotImplementedError
     
     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius
         
         def area(self):
             return 3.14 * self.radius ** 2
     
     class Square(Shape):
         def __init__(self, side):
             self.side = side
         
         def area(self):
             return self.side ** 2
     ```
   - **Library Class:**
     ```python
     class Library:
         def __init__(self):
             self.books = []
         
         def borrow_book(self, book):
             self.books.append(book)
         
         def return_book(self, book):
             self.books.remove(book)
     ```

6. **File Handling:**
   - **Word Frequency Count:**
     ```python
     from collections import Counter
     
     def word_frequency(filename):
         with open(filename, 'r') as file:
             words = file.read().split()
             return Counter(words)
     ```
   - **Merge Files:**
     ```python
     def merge_files(file1, file2, output_file):
         with open(output_file, 'w') as outfile:
             for filename in (file1, file2):
                 with open(filename) as infile:
                     outfile.write(infile.read())
     ```
   - **Parse CSV File:**
     ```python
     import csv
     
     def extract_columns(input_file, output_file, columns):
         with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
             reader = csv.reader(infile)
             writer = csv.writer(outfile)
             for row in reader:
                 writer.writerow([row[i] for i in columns])
     ```

7. **Working with APIs:**
   - **Fetch Data from REST API:**
     ```python
     import requests
     
     def fetch_data(url):
         response = requests.get(url)
         return response.json()
     ```
   - **Simple Flask API:**
     ```python
     from flask import Flask, request, jsonify
     
     app = Flask(__name__)
     
     @app.route('/api', methods=['GET', 'POST'])
     def api():
         if request.method == 'POST':
             data = request.json
             return jsonify(data), 201
         return jsonify({"message": "GET request received"})
     
     if __name__ == '__main__':
         app.run()
     ```
   - **Send Email Using SMTP:**
     ```python
     import smtplib
     
     def send_email(to_email, subject, body):
         with smtplib.SMTP('smtp.example.com', 587) as server:
             server.starttls()
             server.login('your_email@example.com', 'password')
             message = f'Subject: {subject}\n\n{body}'
             server.sendmail('your_email@example.com', to_email, message)
     ```

8. **Data Processing:**
   - **Process Log File:**
     ```python
     def process_log_file(filename):
         with open(filename, 'r') as file:
             for line in file:
                 # Process each line
                 print(line.strip())
     ```
   - **Read Large Dataset in Chunks:**
     ```python
     import pandas as pd
     
     def process_large_csv(filename):
         for chunk in pd.read_csv(filename, chunksize=1000):
             # Process each chunk
             print(chunk.head())
     ```
   - **Generate Summary Report:**
     ```python
     def generate_summary(data):
         summary = {
             'total_entries': len(data),
             'average_value': sum(data) / len(data)
         }
         return summary
     ```

9. **Concurrency and Parallelism:**
   - **Threading Example:**
     ```python
     import threading
     
     def print_numbers():
         for i in range(5):
             print(i)
     
     thread = threading.Thread(target=print_numbers)
     thread.start()
     thread.join()
     ```
   - **Producer-Consumer Problem:**
     ```python
     import threading
     import queue
     
     q = queue.Queue()
     
     def producer():
         for i in range(5):
             q.put(i)
     
     def consumer():
         while True:
             item = q.get()
             if item is None:
                 break
             print(item)
     
     t1 = threading.Thread(target=producer)
     t2 = threading.Thread(target=consumer)
     t1.start()
     t2.start()
     t1.join()
     q.put(None)  # Stop the consumer
     t2.join()
     ```
   - **Multiprocessing Example:**
     ```python
     from multiprocessing import Process, current_process
     
     def worker():
         print(f'Worker: {current_process().name}')
     
     processes = [Process(target=worker) for _ in range(5)]
     for p in processes:
         p.start()
     for p in processes:
         p.join()
     ```

### Advanced Practical Exercises (Optional)

1. **Web Scraping:**
   - **Scrape Data with BeautifulSoup:**
     ```python
     import requests
     from bs4 import BeautifulSoup
     
     def scrape_website(url):
         response = requests.get(url)
         soup = BeautifulSoup(response.text, 'html.parser')
         return soup.title.string
     ```
   - **Multi-Page Scraper:**
     ```python
     def scrape_multiple_pages(base_url, pages):
         for i in range(1, pages + 1):
             url = f"{base_url}/page/{i}"
             print(scrape_website(url))
     ```

2. **Data Analysis with Pandas:**
   - **Load CSV and Analyze:**
     ```python
     import pandas as pd
     
     def analyze_data(filename):
         df = pd.read_csv(filename)
         return df.describe()
     ```
   - **Clean and Preprocess Data:**
     ```python
     def clean_data(df):
         df.fillna(0, inplace=True)  # Handle missing values
         return df
     ```

3. **Automated Testing:**
   - **Unit Tests with Unittest:**
     ```python
     import unittest
     
     class TestMathOperations(unittest.TestCase):
         def test_add(self):
             self.assertEqual(1 + 1, 2)
     
     if __name__ == '__main__':
         unittest.main()
     ```
   - **Test Suite with Pytest:**
     ```python
     import pytest
     
     @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5)])
     def test_addition(a, b, expected):
         assert a + b == expected
     ```

### Django Rest API, Authentication, Authorization, and Deployment Questions

1. **Django Rest API:**
   - **Create DRF View:**
     ```python
     from rest_framework.views import APIView
     from rest_framework.response import Response
     
     class MyAPIView(APIView):
         def get(self, request):
             return Response({"message": "GET request"})
         
         def post(self, request):
             return Response({"message": "POST request"})
     ```
   - **Serializers in DRF:**
     ```python
     from rest_framework import serializers
     
     class MyModelSerializer(serializers.ModelSerializer):
         class Meta:
             model = MyModel
             fields = '__all__'
     ```
   - **Pagination:**
     ```python
     from rest_framework.pagination import PageNumberPagination
     
     class CustomPagination(PageNumberPagination):
         page_size = 10
     ```

2. **Authentication & Authorization:**
   - **User Authentication in Django:**
     ```python
     from django.contrib.auth.models import User
     from rest_framework.authtoken.models import Token
     
     user = User.objects.create_user('username', 'email', 'password')
     token = Token.objects.create(user=user)
     ```
   - **DRF Permissions:**
     ```python
     from rest_framework.permissions import IsAuthenticated
     
     class MyAPIView(APIView):
         permission_classes = [IsAuthenticated]
     ```
   - **Securing Django Apps:**
     - Use `django.middleware.csrf.CsrfViewMiddleware` for CSRF protection.
     - Use `X-Content-Type-Options`, `X-XSS-Protection`, and `Content-Security-Policy` headers.

3. **Deployment:**
   - **Deploying with Nginx and Gunicorn:**
     - Configure Nginx to serve the app via Gunicorn.
   - **Setting Up HTTPS:**
     - Use Let's Encrypt with Certbot to obtain SSL certificates.
   - **Managing Environment Variables:**
     - Use `.env` files with `python-decouple` or `django-environ`.

4. **SQL & ACID Properties:**
   - **ACID Properties:**
     - **Atomicity:** Transactions are all-or-nothing.
     - **Consistency:** Transactions lead to a valid state.
     - **Isolation:** Transactions do not affect each other.
     - **Durability:** Once committed, transactions remain.
   - **Optimizing Slow SQL Queries:** Use indexing, avoid SELECT *, and analyze query plans.
   - **SQL vs NoSQL:** 
     - SQL is relational, structured; NoSQL is non-relational, unstructured.