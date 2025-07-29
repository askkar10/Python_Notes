# private variables and private methods

class Mine:
  def __init__(self):
    self.x = 2
    self.__y = 3
  def print_y(self):
    print(self.__y)

m = Mine()
print(m.x)
# print(m.__y) -> error bo jest to prywatne 
m.print_y