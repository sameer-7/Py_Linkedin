# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.
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
#no output is displayed as we need to create objects to show output