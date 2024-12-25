try:
    a=5;b=0
    c=a/b
except:
    print("Error: Division by zero is not allowed")

try:
    print(x)
    print(5/0)
except NameError:
    print("Variable x is not defined")
except:
    print("An error occurred")

try:
    print("Try Block")
except:
    print("Except Block")
else:
    print("Nothing")
finally:
    print("Finally")

try:
    print("outer try")
    try:
        print("inner try")
        print(10/0)
    except ZeroDivisionError:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("outer except")
finally:
    print("outer finally")