# Base class
class Shape:
    def area(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


# Rectangle class
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


# Square class
class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s


# Triangle class
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


# Main program (Objects)
c = Circle(5)
r = Rectangle(4, 6)
s = Square(4)
t = Triangle(6, 3)

print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())
print("Area of Square:", s.area())
print("Area of Triangle:", t.area())
