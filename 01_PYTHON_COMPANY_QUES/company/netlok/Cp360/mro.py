class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(B, A):
    # pass
    def show(self):
        return "C"

# Create an instance of class C
obj = C()

# Print the output of the show method
print(obj.show())
