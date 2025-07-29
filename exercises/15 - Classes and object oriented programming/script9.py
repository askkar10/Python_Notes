class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,move_x,move_y):
        self.x = self.x + move_x
        self.y = self.y + move_y
    
class Square(Shape):
    def __init__(self, s=1,x=0, y=0):
        super().__init__(x, y)
        self.side = s

class Circle(Shape):
    def __init__(self,r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r

s1 = Square()
s1.move(2,2)
print(s1.side,s1.x,s1.y)
c1 = Circle()
c1.move(4,5)
print(c1.radius,c1.x,c1.y)
c2 = Circle(10,4,2)
print(c2.radius,c2.x,c2.y)