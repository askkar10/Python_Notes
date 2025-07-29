from pathlib import Path

# a)

#path = Path('tekst_path.txt')
#data = 'Witam serdecznie w tym super dzionku.\n'
#data += 'Jest bardzo sympatycznie'
#path.write_text(data)

# b)

#path = Path('tekst_path.txt')
#d = path.read_text()
#print(d)

# c)

#path = Path('binary_path')
#data = b'witam costam 1011'
#path.write_bytes(data)

# d)
path = Path('binary_path')
d = path.read_bytes()
print(d)