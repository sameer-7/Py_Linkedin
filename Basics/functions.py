def funt():
    print("Hello Function")
funt()
funt()
print(funt())

def funct(par_name):
    print("Name is : ",par_name)
funct("Python")

def sq_num(x):
    print("Square is : ",x*x)

def add(x,y):
    return x+y
print(add(10,20))
print(add(10,40))
def add_sub(x,y):
    add = x+y
    sub = x-y
    return add,sub
print(add_sub(90,10))

#Positional arguments
def sub(a,b):
    print(a-b)
sub(100,200)
sub(200,100)

#Keyword arguments
def print_msg(name,msg):
    print("Hello Dear,",name,msg)
print_msg(name = 'Python',msg= '3.11 Version')

def cube_fun(x,y):
    return x**y
#positional
print(cube_fun(2,3))
#positional,keyword
print(cube_fun(2,y=4)) 
#keyword,positional
#print(cube_fun(x=3,4)) => Error

#Default arguments
def def_Arg(name='Python'):
    print(name)
def_Arg('Java')
def_Arg()

#Variable Length arguments
def sum_fun(*n):
    sum=0
    for i in n:
        sum+=i
    return sum
print(sum_fun())
print(sum_fun(10))
print(sum_fun(10,20))
print(sum_fun(10,20,30,40))

#global
a=10;
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()
#local
def f1():
    x=10
    print(x)
def f2():
    print(x)
f1()
#f2() - not valid
e=10
def f1():
    e=777
    print(e)
def f2():
    print(e)
f1()
f2()

r=10 
def f1():
    global r
    r=888
    print(r)
def f2():
    print(r)
f1()
f2()

t=10
def f1():
    t=333
    print(t)
    print(globals()['t'])
f1()

def non_rec_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("Non-Recursive Factorial",non_rec_fact(5))

#Recursive functions
def rec_fact(n):
    if n==0:
        return 1
    else:
        result = n*rec_fact(n-1)
    return result
print("Recursive Factorial",rec_fact(5))

#Anonymous Function - Lambda Function
#lambda arg_list : expression
lf = lambda n:n*n
print(lf(5))

slf = lambda a,b:a+b
print(slf(5,6))

def outer():
    print("Outer")
    def inner():
        print("Inner")
    print("outer calling inner")
    inner()
outer()






