# special methods attributes are marked by double underscore
# __str__ -> user readable string representation of instance
# __init__ -> special method that initialize instance of class

class Color:
  def __init__(self,red,green,blue):
    self.red = red
    self.green = green
    self.blue = blue
  def __str__(self):
    return f"R={self.red:d} G={self.green:d} B={self.blue:d}"

c = Color(15,35,3)
print(c) 

