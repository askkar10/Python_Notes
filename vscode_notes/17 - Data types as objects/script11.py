# __add__ -> pozwala zdefinować jak ma działać operator dodawania '+'
# dla twojej klasy

class Punkt:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self,inny):
    return Punkt(self.x + inny.x,self.y + inny.y)
  def __str__(self) -> str:
    return f"({self.x},{self.y})"

p1 = Punkt(1,2)
p2 = Punkt(3,3)
p3 = p1 + p2
print(p3)