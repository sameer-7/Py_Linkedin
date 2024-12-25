# Similar to list comprehensions, but instead of creating a list, they create a generator object. They use parentheses instead of square brackets.
squared_gen = (x**2 for x in range(10))

for square in squared_gen:
    print(square)
