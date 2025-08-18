Let's break down your questions and address them one by one.

### 1. Finding All Student Names with "Math" as a Subject
Given a dataset like this:

```plaintext
Name    Subject
Ashok   Maths
Danish  Maths,Phy
Xyz     Bio
Abc     Pys,Maths
```

You can use Python with Pandas to filter students who have "Maths" as a subject.

```python
import pandas as pd

# Create the DataFrame
data = {
    'Name': ['Ashok', 'Danish', 'Xyz', 'Abc'],
    'Subject': ['Maths', 'Maths,Phy', 'Bio', 'Pys,Maths']
}
df = pd.DataFrame(data)

# Filter students who have 'Maths' in their Subject
students_with_maths = df[df['Subject'].str.contains('Maths')]

# Display the results
print(students_with_maths)
```

### 2. How to Drop Null Values in Pandas
To drop rows with `NaN` (null) values in a Pandas DataFrame:

```python
import pandas as pd

# Sample DataFrame with NaN values
data = {
    'Name': ['Ashok', 'Danish', None, 'Abc'],
    'Subject': ['Maths', 'Maths,Phy', 'Bio', None]
}
df = pd.DataFrame(data)

# Drop rows with any NaN values
df_cleaned = df.dropna()

# Display the cleaned DataFrame
print(df_cleaned)
```

You can also drop rows or columns based on specific criteria, like dropping rows if **all** columns are NaN:

```python
df_cleaned = df.dropna(how='all')
```

Or drop columns instead of rows:

```python
df_cleaned = df.dropna(axis=1)  # axis=1 means columns
```

### 3. MRO (Method Resolution Order) in Python
MRO determines the order in which base classes are searched when executing a method. Python follows the C3 linearization algorithm for MRO.

You can view the MRO of a class using the `__mro__` attribute or `mro()` method:

```python
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

# Check the Method Resolution Order
print(D.__mro__)
```

This will print the order in which methods are resolved when called from an instance of class `D`.

### 4. Design Pattern Using Classes
Here's an example of the Singleton Design Pattern using a Python class:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

# Usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
```

This pattern ensures that only one instance of the `Singleton` class is created.

### 5. MySQL Storage Engines
MySQL offers several storage engines, including:

- **InnoDB:** The default storage engine that supports ACID-compliant transactions, foreign keys, and row-level locking.
- **MyISAM:** An older storage engine known for its speed, but it does not support transactions or foreign keys.
- **Memory:** Stores all data in RAM for faster access, but data is lost when the server shuts down.
- **CSV:** Stores data in comma-separated values (CSV) format.
- **ARCHIVE:** Used for storing large amounts of data that seldom need to be retrieved.
- **MERGE:** Allows multiple MyISAM tables to be treated as a single table.

### 6. Write Indexing in SQL
To create an index in SQL:

```sql
CREATE INDEX index_name
ON table_name (column_name);
```

For example:

```sql
CREATE INDEX idx_subject ON students(Subject);
```

### 7. Compound Index
A compound index (multi-column index) is an index on multiple columns. It is created like this:

```sql
CREATE INDEX idx_name_subject ON students(Name, Subject);
```

This index will be used when queries filter by `Name`, `Subject`, or both. It’s useful when you frequently query by multiple columns together.

---

This should cover the topics you asked about. If you have any more specific questions or need further clarification on any of these topics, feel free to ask!



Sure! Let's dive deeper into **Method Resolution Order (MRO)** and **Design Patterns** with more examples.

### Method Resolution Order (MRO) in Python

MRO determines the order in which methods are resolved when multiple inheritance is involved. Python follows the C3 linearization algorithm (also known as the C3 superclass linearization) to determine this order.

#### Example 1: Diamond Problem
Consider the classic "diamond problem" in multiple inheritance:

```python
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

d = D()
d.method()

# Check MRO
print(D.mro())
```

**Explanation:**
- `D` inherits from both `B` and `C`, which both inherit from `A`.
- When `d.method()` is called, Python needs to figure out which `method` to execute. The MRO helps in resolving this by defining the order.
- The output of the MRO in this case will be `[D, B, C, A, object]`.

#### Example 2: Multiple Inheritance with Unrelated Classes
Another example:

```python
class X:
    def method(self):
        print("Method from X")

class Y:
    def method(self):
        print("Method from Y")

class Z(X, Y):
    pass

z = Z()
z.method()

# Check MRO
print(Z.mro())
```

**Explanation:**
- `Z` inherits from `X` and `Y`.
- When `z.method()` is called, the method from `X` is executed because `X` comes before `Y` in the MRO list.
- The MRO will be `[Z, X, Y, object]`.

#### Example 3: Custom Class Hierarchy
Let's create a more complex class hierarchy:

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    def method(self):
        print("D method")

class E(C):
    def method(self):
        print("E method")

class F(D, E):
    pass

f = F()
f.method()

# Check MRO
print(F.mro())
```

**Explanation:**
- This example shows a complex hierarchy where `F` inherits from both `D` and `E`.
- The method resolution order for `F` is `[F, D, B, E, C, A, object]`, so when you call `f.method()`, it will execute the method in `D`.

### Design Patterns

Design patterns are reusable solutions to common problems in software design. Here are some more examples:

#### 1. **Factory Method Pattern**
The Factory Method Pattern provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.

```python
class Button:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Render a button in a Windows style")

class HTMLButton(Button):
    def render(self):
        print("Render a button in HTML style")

class Dialog:
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        button.render()

class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()

# Client code
def client_code(dialog: Dialog):
    dialog.render()

client_code(WindowsDialog())  # Output: Render a button in a Windows style
client_code(WebDialog())      # Output: Render a button in HTML style
```

**Explanation:**
- `Dialog` is the base class, and `WindowsDialog` and `WebDialog` are its subclasses.
- The `create_button` method is a factory method that allows subclasses to create their own specific types of buttons.

#### 2. **Observer Pattern**
The Observer Pattern allows an object (subject) to notify other objects (observers) when its state changes.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer:
    def update(self, subject: Subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject: Subject):
        print(f"Observer: Reacting to state change to {subject.state}")

# Client code
subject = ConcreteSubject(10)
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.state = 20  # Both observers will be notified and react to the state change
```

**Explanation:**
- The `Subject` manages a list of observers and notifies them when its state changes.
- Observers can subscribe to or unsubscribe from the subject.
- When the subject's state changes, all registered observers are notified.

#### 3. **Strategy Pattern**
The Strategy Pattern enables selecting an algorithm's behavior at runtime.

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# Client code
data = [1, 3, 2, 4, 5]

context = Context(ConcreteStrategyA())
print("Ascending:", context.execute_strategy(data))  # Output: [1, 2, 3, 4, 5]

context.set_strategy(ConcreteStrategyB())
print("Descending:", context.execute_strategy(data))  # Output: [5, 4, 3, 2, 1]
```

**Explanation:**
- `Strategy` defines a family of algorithms.
- The `Context` uses a `Strategy` object to perform its algorithm. The algorithm can be switched at runtime.

---

These additional examples should give you a more in-depth understanding of both MRO and design patterns. If you need further explanations or have specific scenarios in mind, feel free to ask!