# Decorators are a way to modify or enhance functions or methods. They are higher-order functions that take a function as an argument and return a new function.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()