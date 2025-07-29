# an oddity with class variables

class Circle:
  pi = 3.14159
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return self.radius * self.radius * Circle.pi

c = Circle(3)
print(c.pi)
c1 = Circle(1)
c2 = Circle(2)
print(c1.pi)
print(c2.pi)
c1.pi = 3.14
print(c.pi)
print(c1.pi)
print(c2.pi)
print(Circle.pi)
print(c2.__class__.pi)