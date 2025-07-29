# __setitem__ -> to specjalna metoda w pythonie, która pozwala na zdefiniowanie obiektu
# przy przypiswaniu wartości za pomoca nawiasó kwadratowych, czyli   -> obj[key] = value

class MojSlownik:
  def __init__(self):
    self.dane = {}
  def __setitem__(self,klucz,wartosc):
    print(f"ustawiam {klucz} na {wartosc}")
    self.dane[klucz] = wartosc
  def __getitem__(self,klucz):
    return self.dane[klucz]

s = MojSlownik()
s['a'] = 10
print(s['a'])