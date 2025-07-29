# class variables
class Circle:
  pi = 3.14159
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return self.radius * self.radius * Circle.pi

print(Circle.pi)
Circle.pi = 4
print(Circle.pi)
Circle.pi = 3.14159

c = Circle(10)
print(c.area())

print(c.__class__.pi)