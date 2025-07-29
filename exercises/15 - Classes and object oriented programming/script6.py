class Circle():
    pi = 3.14
    def __init__(self,r=1):
        self.radius = r
    def area(self):
        return (self.radius * self.radius * Circle.pi)

c = Circle(7)
print(c.__class__.pi)
print(c.pi)
print(c.area())
c.radius = 8
print(c.area())