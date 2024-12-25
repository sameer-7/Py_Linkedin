d = {1:'a',
     2:'b',
     3:'c',
     4:'d'
     }
print(d)
#Methods
print(d.items())
print(d.keys())
print(d.values())
print(d.get(3))
d.update({5:'e',6:'f'})
print(d)
d.pop(5)
print(d)
d.popitem()
print(d)
copy_d = d.copy()
print(copy_d)
d=d.setdefault(9,'i')
print(d)
d1={'name':'Python','version':3.10}
d1.clear()