class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Create a Circle instance from a diameter."""
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def area(radius):
        """Calculate the area of a circle given its radius."""
        return Circle.pi * (radius ** 2)

# Using the class method to create an instance
circle1 = Circle.from_diameter(10)
print(f"Circle with radius {circle1.radius}")

# Using the static method to calculate the area
area_of_circle = Circle.area(circle1.radius)
print(f"Area of the circle: {area_of_circle}")
