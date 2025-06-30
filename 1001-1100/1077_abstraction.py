from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

def main():
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]
    for shape in shapes:
        print(f"{shape.__class__.__name__}:")
        print(f"  Area: {shape.area()}")
        print(f"  Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    main()