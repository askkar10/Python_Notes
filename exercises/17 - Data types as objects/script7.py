class MojSlownik:
    def __init__(self):
        self.dane = {}
    def __setitem__(self,klucz,wartosc):
        print(f'Ustawiam {klucz} na {wartosc}')
        self.dane[klucz] = wartosc
    def __getitem__(self,klucz):
        return self.dane[klucz]
    
m = MojSlownik()
m['apple'] = 'jabłko'
print(m['apple'])