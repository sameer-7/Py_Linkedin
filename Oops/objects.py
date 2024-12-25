class Dog:
    #class attributes
    species = 'Canis familiaris'
    #Initializer/ constructor
    def __init__(self,name,age):
        #Instance attribute
        self.name = name
        self.age = age
    #Method to display information
    def describe(self):
        return f"{self.name} is {self.age} years old and belongs to species {self.species}"
# An object is an instance of a class. It represents a specific entity with the attributes and methods defined in the class.
#creating instance 
dog1 = Dog("Buddy",3)
dog2 = Dog("Max",5)
#accessing objects
print(dog1.name)
print(dog2.name)
#calling methods
print(dog1.describe())