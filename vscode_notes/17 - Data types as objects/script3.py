class A:
  pass
class B(A):
  pass

b = B()
print(type(b))
print(b.__class__)
b_class = b.__class__
print(b_class == B)
print(b_class.__name__)
print(b_class.__bases__) # __bases__ -> finding out class and class inherits from