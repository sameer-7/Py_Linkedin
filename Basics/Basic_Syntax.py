#Display Hello Python
print("Hello Python 3.10")

#Comments

#Python singleline comments are written using '#' symbol

#Python multiline comments are written using '''Multi Line use ''' triple quotes

#Variables
a = 10 #declaring variable
print (a) #displaying variable

#user input
b = input("Enter value of b : 7");
print(b) #displaying user input

#Indentation
for i in range(1,10):
    #above 4 spaces are indentation
    print(i, end = ' ')
if 5>3:
    print(5>3)

#How to know type of variable declared
var = 'Character'
var_1 = 5
var_2 = 15.678
var_3 = False
var_4 = [9,8,6]
var_5 = (2,4,5)
var_6 = {2,2,4}
print(type(var))
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
print(type(var_5))
print(type(var_6))

print("This print is for backslash n \n------Nextline")

variable = 1+2+3+\
           4+5+6+\
           7+8+9
print(variable)

#Implicit Continuation
l_list = [
    1, 2, 3,
    4, 5, 6,
]
print(l_list)
#Explicit Continuation (\) escape sequence character
s_string = 'Explicit'\
'Continuation'
print(s_string)

num1 = 10;num2 = 20; n_sum = num1+num2;print('nsum : ',n_sum)
