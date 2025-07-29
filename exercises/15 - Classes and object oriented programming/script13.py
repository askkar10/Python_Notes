class Temperature:
    def __init__(self):
        self._temp_fahr = 0
    @property
    def temp(self):
        return f"{((self._temp_fahr-32) * 5/9):.2f}"
    @temp.setter
    def temp(self,new_temp):
        self._temp_fahr = new_temp *9/5 + 32

t = Temperature()
print(t._temp_fahr)
print(t.temp)
t. temp = 34
print(t.temp)
print(t._temp_fahr)