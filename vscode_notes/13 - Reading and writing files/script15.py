# shelve -> to wygodne narzędzie do trwałego przechowywania obiektów pythona w sposób przypominający słownik
# shelve w keys moze miec tylko string, nie moze miec cyfry jako klucza

import shelve
book = shelve.open('addresses')

book['flinstone'] = ('fred','555-1234','1233 Bedrook Place')
book['rubble'] = ('barres','555-4321','1235 Bedrook Place')
book.close()