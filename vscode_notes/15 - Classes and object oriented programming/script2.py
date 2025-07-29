# using a class intance as a structure or record

class Circle:
  pass

my_circle = Circle()
my_circle.radius = 5
print(2*3.14*my_circle.radius)

class Circle:
  def __init__(self):
    self.radius = 1

my_circle = Circle()
print(2*3.14*my_circle.radius)
my_circle.radius = 5
print(2*3.14*my_circle.radius)