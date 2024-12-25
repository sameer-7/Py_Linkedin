#Numeric type
int_dt = 89
print(int_dt)
print(type(int_dt))
float_dt = 56.894
print(float_dt )
print(type(float_dt))
complex_dt = 2+1j
print(complex_dt)
print(type(complex_dt))
#Boolean type
bool_dt = True
print(bool_dt)
print(type(bool_dt))
#Text type
str_dt = "String_Datatype"
print(str_dt)
print(type(str_dt))
print("Accessing String Elements : ",end=' ')
print([i for i in str_dt])
#None type
none_dt = None
print(none_dt)
print(type(none_dt))
#Sequences types
list_dt = [1,2,4,9,16,25]
print(list_dt)
print(type(list_dt))
print("Accessing list Elements : ",end= ' ')
print([i for i in list_dt])
print("Changing List Elements")
list_dt[0] = 100;list_dt[1] = 200;list_dt[-1] = 500;
print("Updated list : ",list_dt)
tuple_dt = 1,2,3,4,5,6,7,8,9
print(tuple_dt)
print(type(tuple_dt))
print("Accessing tuple Elements : ",end= ' ')
print([i for i in tuple_dt])
print("Unable to update tuple")
# tuple_dt[-1] = 5
#Mapping types
dict_dt = {1:'a', 2:'b', 3:'c', 4:'d'}
print(dict_dt)
print(type(dict_dt))
print("Accessing dict Elements : ",end= ' ')
print([dict_dt[i] for i in range(1,4)])
print("DICT_DT.ITEMS : ",dict_dt.items())
dict_dt_a = {1:'Ford', 2:'Toyota', 3:'TATA', 4:'Mahindra'}
print("Fetch using direct index",dict_dt_a[3])
print("Fetch using get function",dict_dt_a.get(3))
#Set types
set_dt = {1,2,2,3,4,5,4,3,2,1}
print(set_dt)
print(type(set_dt))
print("Accessing set Elements : ",end= ' ')
print("No index is supported")
print([set_dt])
print([i for i in set_dt])
frozenset_dt = frozenset(set_dt)
print(frozenset_dt)
print(type(frozenset_dt))
#Binary types
bytes_dt = b"bytesdatatype"
print(bytes_dt)
print(type(bytes_dt))
bytearray_dt = bytearray(19)
print(bytearray_dt)
print(type(bytearray_dt))
memoryview_dt = memoryview(bytes(19))
print(memoryview_dt)
print(type(memoryview_dt))

x=5;
print(bin(x))
print(oct(x))
print(hex(x))
print(ord('A'))
print(chr(x))