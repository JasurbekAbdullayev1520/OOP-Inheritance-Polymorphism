class Shape:
    def __init__(self,name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def area(self):
        return f"{self.name} yuzi: {self.a * self.b}kv"

class Circle(Shape):
    def __init__(self, name, p, r):
        self.name = name
        self.p = p
        self.r = r

    def area(self):
        return f"{self.name} yuzi: {2 * self.p * self.r ** 2}kv"


class Rectangle(Shape):
    pass

class Triangle(Shape):
    def __init__(self,name, a, b, h):
        self.name = name
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return f"{self.name} yuzi: {self.a * self.b * self.h / 2}kv"

p = Circle("Doira", 3.14, 6)
p1 = Rectangle("Tortburchak", 3, 6)
p2 = Triangle("Uchburchak", 2, 4, 2)

print(p.area())
print(p1.area())
print(p2.area())