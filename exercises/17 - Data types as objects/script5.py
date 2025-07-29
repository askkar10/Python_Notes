class Color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self):
        return f"R:{self.red:d} G:{self.green:d} B:{self.blue:d}"
    
c1 = Color(10,20,30)
c2 = Color(255,255,255)
print(c1)
print(c2)