#IF conditional statement
#IF statement is used to execute a block of code if a certain condition is met.
#The syntax of the IF statement is as follows:
#IF condition:
#    # code to be executed if the condition is true
#ELSE:
#    # code to be executed if the condition is false
#IF-ELSE statement
#IF-ELSE statement is used to execute a block of code if a certain condition is met,
#and another block of code if the condition is not met.
#The syntax of the IF-ELSE statement is as follows:
#IF condition:
#    # code to be executed if the condition is true
#ELSE:
#    # code to be executed if the condition is false
#IF-ELIF-ELSE statement
#IF-ELIF-ELSE statement is used to execute a block of code if a certain condition
#is met, another block of code if another condition is met, and another block of code
#if the conditions are not met.
#The syntax of the IF-ELIF-ELSE statement is as follows:
#IF condition1:
#    # code to be executed if the condition1 is true
#ELIF condition2:
#    # code to be executed if the condition2 is true
#    # code to be executed if the condition1 is false and condition2 is true
#ELSE:
#    # code to be executed if the conditions are not met
#Simple if
letter = 'a'
if letter=='a':
    print("Letter is a")

if letter=='a':
    print("letter is a")
else:
    print("letter is b")

if letter=='a':
    print("letter is a")
elif letter == 'b':
    print("letter is b")
elif letter=='c':
    print("letter is c")
else:
    print("letter is d")

letter = "A"
if letter == "B":
    print("Letter is B")
else:
    if letter == "C":
        print("Letter is C")
    else:
        if letter == "A":
            print("Letter is A")
        else:
            print("Letter is not A,B,C")

#Ternary Expression conditional statement
a,b = 10,20
print("Both are equal" if a==b else "a>b" if a>b else "a<b")

#Arithmetic operators
a=10;b=20;
print("Add : ",a+b)
print("Sub : ",a-b)
print("Prod : ",a*b)
print("Div : ",a/b)
print("Rem : ",a%b)
print("Fldiv : ",a//b)

sum_a_b = 0
sum_a_b = sum_a_b + a+b
print("Sum_a_b : ",sum_a_b)

#Assignment Operators
a = 10
print(a)
a+=3
print(a)
a-=3
print(a)
a*=3
print(a)
a/=3
print(a)
a%=3
print(a)
a//=3
print(a)
a**=3
print(a)
# a&=3
# print(float(a))
# a|=3
# print(a)
# a^=3
# print(a)
# a>>=3
# print(a)
# a<<=3
# print(a)
# print(a:=3)

#Comparison Operators
#Relational operators are used to compare two values and return a boolean value.
#The relational operators are as follows:
#1. Equal to: a == b
#2. Not Equal to: a != b
#3. Greater than: a > b
#4. Less than: a < b
#5. Greater than or equal to: a >= b
#6. Less than or equal to: a <= b

a=50;b=100
print(a==b) #False
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b) #False

#Logical Operators
#Logical operators are used to combine multiple conditions and return a boolean value.
#The logical operators are as follows:
#1. AND: a and b
#2. OR: a or b
#3. NOT: not a

a=10;b=5
if a==5 and b==5:
    print("Both are equal")
elif a>b or a<b:
    print("a is greater")
else:
    print("b is greater")

print(not(a))

#Membership Operators
#in, not in
#Membership operators are used to check if a value is present in a sequence or not.
#The membership operators are as follows:
#1. in: a in b
#2. not in: a not in b
a=[1,2,3,4,5]
print(3 in a) #True
print(6 not in a) #True

#Identity Operators
#is, is not
#Identity operators are used to check if two variables point to the same object in memory or not.
#The identity operators are as follows:
#1. is: a is b
#2. is not: a is not b
a=10;b=10
print(a is b) #True
print(a is not b) #False

#Bitwise Operator
#Bitwise operators are used to perform operations on the bits of a number.
#The bitwise operators are as follows:
#1. & (bitwise AND)
#2. | (bitwise OR)
#3. ^ (bitwise XOR)
#4. ~ (bitwise NOT)
#5. << (left shift)
#6. >> (right shift)
a=5;b=3
print(a&b) #3
print(a|b) #7
print(a^b) #6
print(~a) #-6
print(a<<1) #10
print(a>>1) #2

#Operator Precedence
#Operator precedence is the order in which operators are executed when there are multiple operators in an expression.
#The operators are grouped into several categories, with the highest precedence operators being executed first.
#The operator precedence in Python is as follows:
#0. Parentheses ()
#1. Exponentiation: **
#2. Multiplication and Division: *, /, //, %
#3. Addition and Subtraction: +, -
#4. Comparison: ==, !=, >, <, >=, <=
#5. Logical AND: and
#6. Logical OR: or
#7. Assignment: =, +=, -=, *=, /=, //=, %=, **
#8. Bitwise: & , |, ^, ~, <<, >>
#9. Membership: in, not in
#10. Identity: is, is not
#11. Logical NOT: not
#12. Unpacking: *
#13. Augmented: +=, -=, *=, /=, //=, %=, **=
#14. Lambda: lambda

#Operator Precedence Example
#In the following example, the expression 2 + 3 * 4 is evaluated as follows
#1. The multiplication operator * is executed first, because it has a higher precedence than the addition
# operator +. So, 3 * 4 is evaluated first, which results in 12
#2. Then, the addition operator + is executed, which results in 14
print(2 + 3 * 4) #14
print((3+9+5)*9%(6/2+8)or(7-8*4)<<5==40)

