# inheritance
class Shape:
  def __init__(self,x,y):
    self.x = x 
    self.y = y
  def move(self,delta_x,delta_y):
    self.x = self.x + delta_x
    self.y = self.y + delta_y  
class Square(Shape):
  def __init__(self,side=1,x=0,y=0):
    super().__init__(x,y)
    self.side = side

class Circle(Shape):
  def __init__(self,r=1,x=0,y=0):
    super().__init__(x,y)
    self.r = r
  
c = Circle(1)
c.move(3,4)
print(f"c.x={c.x} c.y={c.y}")