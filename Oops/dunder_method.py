# Dunder methods (double underscore methods), also known as magic methods, allow you to define the behavior of your objects for built-in functions and operators. They enable operator overloading and object representation.
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point({self.x},{self.y})"
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y)
p1 = Point(1,2)
p2 = Point(3,4)
print(p1)
print(p2)
p3 = p1+p2
print(p3)