# An iterator is an object that implements the iterator protocol, consisting of the methods __iter__() and __next__(). It allows you to traverse through all the elements in a collection.
class MyIterator:
    def __init__(self,max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max:
            self.current +=1
            return self.current-1
        else:
            raise StopIteration
for num in MyIterator(5):
    print(num)
