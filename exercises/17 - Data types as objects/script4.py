class C:
    pass
class D:
    pass
class E(D):
    pass

x = 12
c = C()
d = D()
e = E()

print(isinstance(c,D))
print(isinstance(d,D))
print(isinstance(d,E))
print(isinstance(e,D))
print('----')
print(issubclass(C,D))
print(issubclass(E,D))
print(issubclass(D,E))