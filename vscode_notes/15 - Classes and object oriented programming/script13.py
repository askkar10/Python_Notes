# using @property for more flexible instance variables

class Temperature:
  def __init__(self):
    self._temp_fahr = 0
  @property
  def temp(self):
    return (self._temp_fahr - 32) * 5 / 9
  @temp.setter
  def temp(self,new_temp):
    self._temp_fahr = new_temp * 9 / 5 + 32

t = Temperature()
print(t._temp_fahr)
print(t.temp)
t.temp = 34
print(t._temp_fahr)
t._temp_fahr = 120
print(t.temp)