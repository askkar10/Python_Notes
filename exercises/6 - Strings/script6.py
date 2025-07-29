a = '    aaaaskaniusz'
b = 'akaniusz          '
c = '        askaniusz      '
print(a.lstrip(),b.rstrip(),c.strip())

a = 'askaniuszaaaa'
print(a.strip('aszk'))
x = 'www.onet.pl'
print(x.removeprefix('www.'),x.removesuffix('.pl'))
e = x.removesuffix('.pl').removeprefix('www.')
print(e)