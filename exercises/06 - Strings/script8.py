y = 'mississipi'
z = y.replace('ss','++')
print(z)
a = '1 2 3 4'
table = a.maketrans('1234','abcd')
b = a.translate(table)
print(b)
tabel = a.maketrans("","",'1 2')
c = a.translate(tabel)
print(c)