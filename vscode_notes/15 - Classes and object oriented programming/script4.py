# methods 

class Circle:
  def __init__(self):
    self.radius = 1
  def area(self):
    return self.radius * self.radius * 3.14159

c = Circle()
c.radius = 3
print(c.area())


class Circle:
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return self.radius * self.radius * 3.14159

c4 = Circle(4)
print(c4.area())
c5 = Circle(5)
print(c5.area())