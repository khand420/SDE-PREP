class DemoA:
    def __init__(self):
        self.__num1 = 5  # Private variable

    def get_num1(self):
        return self.__num1


class DemoB(DemoA):
    def __init__(self):
        super().__init__()
        self.__num1 = 6  # This is a different variable due to name mangling

    def get_num1(self):
        return self.__num1


# Create instances of DemoA and DemoB
demo_a = DemoA()
demo_b = DemoB()

# Print the outputs
print(demo_a.get_num1(), demo_b.get_num1())
