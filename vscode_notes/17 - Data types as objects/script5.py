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
print(isinstance(x,E))
print(isinstance(c,E))
print(isinstance(e,E))
print(isinstance(e,D))
print(isinstance(d,E))
y = 12
print(isinstance(y,type(5)))
print('----')
print(issubclass(C,D))
print(issubclass(E,D))
print(issubclass(D,D))
print(issubclass(e.__class__,D))