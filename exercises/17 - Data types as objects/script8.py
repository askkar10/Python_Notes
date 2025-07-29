class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,inny):
        return Punkt(self.x+inny.y,self.y+inny.y)
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1 = Punkt(0,0)
p2 = Punkt(11,15)
p3 = p1 + p2
print(p3)