# @staticmehtod decorator

"""cricle module : contains the Circle class"""
class Circle:
  """Circle class"""
  all_circles = []
  pi = 3.13159
  def __init__(self,r=1):
    """Create a circle with the given radius"""
    self.radius = r
    self.__class__.all_circles.append(self)
  def area(self):
    "determine the are of the circle"
    return self.__class__.pi * self.radius * self.radius

  @staticmethod
  def total_area():
    """static method to total of the areas of all circles"""
    total = 0
    for c in Circle.all_circles:
      total = total + c.area()
    return total

c1 = Circle(1)
c2 = Circle(2)
print(Circle.total_area())
c2.radius = 3
print(Circle.total_area())

# documentatnion
print(Circle.__doc__)
print(Circle.area.__doc__)