#alphanumeric variables are allowed
#no variable starts with special symbol or number
#only _ is valid
#no space is allowed in between of variables
# X and x is different
#can't use python keywords as variables

variable123 = 789454
_variable = 458.5698
VARIABLE = 986278951
# VAR IABLE = "Invalid variable"
# $variable = "Invalid variable"
# 1variable = "Invalid variable"

number_declare : int
number_declare = 50
print(__annotations__)
print(number_declare)
print(type(number_declare))
print(id(number_declare))

char_var = 'c'
str_var = "String Variable"
int_var = 123456
float_var = 12345.6789
bool_var = True
list_var = [1,2,3,4,5]
tuple_var = 1,2,3,4,5
set_var = {1,2,2,3,2,3}
dict_var = {1:'a',2:'b',3:'c'}
STR_VAR = "STRING VARIABLE"

print(id(int_var))
print(id(bool_var))
print(id(STR_VAR))
print(id(str_var))

#snake case name_of_variable
#camel case nameOfVariable
#pascal case NameOfVariable

_Variable =190 #private variable

# restricted variables list
import keyword
keyword.kwlist
print("List of Reserved Keywords",keyword.kwlist)

# local
# nonlocal
# global

global_var = 'global'
def base_fun():
    nonlocal_var = 'nonlocal';
    def in_base_fun():
        local_var = 'local';
        print(f"Hi from the '{local_var}' scope!")
        print(f"Hi from the '{nonlocal_var}' scope!")
        print(f"Hi from the '{global_var}' scope!")
    in_base_fun()

# from variables import base_fun
base_fun()
