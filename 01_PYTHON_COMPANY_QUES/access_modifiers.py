
#1 Public members: These can be accessed from anywhere, both inside and outside the class. By default, all members are public.

class MyClass:
    def __init__(self):
        self.public_var = "I am public"
    
    def public_method(self):
        print("This is a public method")

obj = MyClass()
print(obj.public_var)  # Accessing public attribute
obj.public_method()    # Calling public method




# 2 Protected members: These are intended to be accessed only within the class and its subclasses. In Python, this is indicated by a single underscore prefix (_). This is a convention and does not prevent access from outside the class.

class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"
    
    def _protected_method(self):
        print("This is a protected method")

obj = MyClass()
print(obj._protected_var)  # Accessing protected attribute
obj._protected_method()    # Calling protected method




# 3 Private members: These are intended to be accessed only within the class itself. In Python, this is indicated by a double underscore prefix (__). This triggers name mangling, where the member name is changed internally to include the class name, making it harder to access from outside.
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"
    
    def __private_method(self):
        print("This is a private method")

    def access_private_method(self):
        self.__private_method()

obj = MyClass()
# print(obj.__private_var)  # This will raise an AttributeError
# obj.__private_method()    # This will raise an AttributeError

# Accessing private members using name mangling
print(obj._MyClass__private_var)
obj._MyClass__private_method()




class Test:
    a = 3
    _b = 4
    __c = 5


print(Test.a)
print(Test._b)
print(Test._Test__c)
