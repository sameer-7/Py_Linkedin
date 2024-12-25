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