# string -> compare with string constants such as 'digits' or 'whitespace'
import string
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# re -> search and replace text using regular expression
import re
string = 'askaniusz'
regexp = re.compile('askaniusz')
x = regexp.search(string)
print(x)

# struct -> interpret bytes as packed binary data and read and write structure data to/from files
import struct
struct.pack('>h', 1023)
struct.pack('<h', 1023)

# difflib -> use helpers for computer deltas, find diffrences between string or sequences, and create patches and diff files
import difflib
a = "qabxcd"
b = "abycdf"
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
    
# textwrap -> wrap and fill text and format text by breaking lines or adding spaces
import textwrap 
print(textwrap.shorten("Hello  world!", width=12))
print(textwrap.shorten("Hello  world!", width=11))

