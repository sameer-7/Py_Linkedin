#Parent class
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} make a sound."
#Child class inherit from parent
class Cat(Animal):
    #overriding method
    def speak(self):
        return f"{self.name} say meow."
#Instance of class
cat = Cat("Whiskers")
print(cat.speak())
dog = Animal("Dog")
print(dog.speak())