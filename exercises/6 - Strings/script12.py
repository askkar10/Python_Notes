a = 'askaniusz'
b = 'karpowicz'
c = 'Imie: {0}, nazwisko: {1}'.format('askaniusz','karpowicz')
d = 'Imie: {0}, nazwisko: {1}'.format(a,b)
e = 'Imie: {name}, nazwisko {surname}'.format(name='askaniusz',surname='karpowicz')
print(c)
print(d)
print(e)

f = 'Imie: {0:$>12}, nazwisko: {2}'.format(a,40,b)
print(f)
