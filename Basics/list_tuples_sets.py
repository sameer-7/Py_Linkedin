# list
a="a","b","c",1,1.2,True,None
l = list(a)
print(l)
print(l[1])
for i in l:
    print(i)
print(l[2::])
#list methods
l.append(5)
print(l)
l.extend(["extend1","extend2"])
print(l)
l.insert(5,"inserted item")
print(l)
l.remove(1)
print(l)
l.pop()
print(l)
l.index("inserted item")
print(l.count('a'))
l2=[1,1,6,7,8,9,4,3,2]
l=l2.sort()
print(l)
l2.reverse()
copy_l = l2.copy()
l2.clear()
#tuple
t=(1,2,3,4,5)
print(t)
#tuple methods
t.count(2)
t.index(3)
slice_t = t[1:3]
print(slice_t)
new_t = t+(6,7)
print(new_t)
repeat_t = t*2
print(repeat_t)
#sets
s={1,2,3,4,5}
print(s)
#methods
s.add(9)
print(s)
s.update([4,5])
print(s)
s.remove(2)
print(s)
s.discard(5)
print(s)
s1=s.pop()
print(s1)
copy_s = s.copy()
print(copy_s)
s.clear()
print(s)
a = {1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))