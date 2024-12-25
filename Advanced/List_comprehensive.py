# List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and can include if clauses.
square = [x**2 for x in range(10)]
print(square)

even_sq = [x**2 for x in range(10) if x%2==0]
print(even_sq)