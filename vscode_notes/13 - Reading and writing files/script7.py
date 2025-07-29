# no open or close are required
from pathlib import Path
p_text = Path('myfile3.txt')
# p_text.write_text('Some text...') # napisanie tekstu

print(p_text.read_text()) # odczytanie tekstu

p_binary = Path('binary-output2.txt')
# p_binary.write_bytes(b'01010011 01101001 01100101 01101101 01100001 00100000 01110011') # napisanie w binary
print(p_binary.read_bytes()) # odczytanie binary