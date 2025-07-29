class Circle():
    pi = 3.14
    all_circles = []
    def __init__(self,radius):
        self.radius = radius
        self.__class__.all_circles.append(self) # lub moze też byc bez __class__
    def area(self):
        return Circle.pi * self.radius * self.radius
    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return f"{total:.2f}"

c1 = Circle(2)
c2 = Circle(4)
print(c1.area())
print(c2.area())
print(Circle.total_area())
print(c1.total_area())