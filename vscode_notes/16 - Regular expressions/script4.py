# raw string don't rpcoes special sequences like \n \t itp.
print(r'Hello' == r'Hello')
print(r'\the' == r'\the')
print(r'\the')
print('\the')

import re
regexp = re.compile(r'\\ten') 
count = 0
file = open('textfile2','r')
for line in file.readlines():
  if regexp.search(line):
    count = count + 1
file.close()
print(count)