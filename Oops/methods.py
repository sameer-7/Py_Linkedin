# Methods are functions defined within a class that operate on instances of that class. They can manipulate object attributes and can be classified into instance methods, class methods, and static methods.
# Instance Methods: Operate on the instance of the class and can access instance variables.
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def display_info(self):
        return f"Car make : {self.make}, Model : {self.model}"
my_car = Car("Toyota","Camry")
print(my_car.display_info())
# Class Methods: Operate on the class itself and can access class variables. They are defined using the @classmethod decorator.
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius = radius
    @classmethod
    def circle_area(cls,radius):
        return cls.pi*radius**2
print(Circle.circle_area(10))
# Static Methods: Do not access or modify the state of the class or instance. They are defined using the @staticmethod decorator.
class Math:
    @staticmethod
    def add(x,y):
        return x+y
print(Math.add(5,3))