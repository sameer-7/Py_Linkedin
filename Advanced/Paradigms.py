# Different approaches to programming supported by Python.
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} says woof!"
    
dog = Dog("Buddy")
print(dog.bark())