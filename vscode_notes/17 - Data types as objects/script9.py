class test:
  def __init__(self,dane):
    self.dane = dane
  def __getitem__(self,index):
    return self.dane[index]

lista = test([10,20,30,40,50])
for number in lista:
  print(number)