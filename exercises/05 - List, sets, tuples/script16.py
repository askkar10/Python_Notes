a = [1,2,3,4,5,1,1,1,1,2,3,5,10,2,3]
b = (1,2,3,4,5,6,7,8,9,10)
b = set(b)
a = set(a)
a.add(200)
print(a)
print(b)
print(a^b)
print(a&b)
print(a|b)
b = frozenset(b)
c = 'programowanie'
c = set(c)
print(c)
d = 'programowanie'
q = list(d)
e = tuple(d)
print(q,e)