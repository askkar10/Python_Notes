# 3 różne sposoby zapisania, żeby wyszukiwało zdanie zaczynające się na wielką lub małą litere
# regexp = re.compile('hello|Hello') 
# regexp = re.compile('(h|H)ello')
# regexp = re.compile('[hH]ello')


import re
regexp = re.compile('hello')
regexp2 = re.compile('hello|Hello')
regexp3 = re.compile('(h|H)ello')
regexp4 = re.compile('[hH]ello')
count_regexp = 0
count_regexp2 = 0
count_regexp3 = 0
count_regexp4 = 0
file = open('textfile','r')
for line in file.readlines():
  if regexp.search(line):
    count_regexp = count_regexp + 1
file.close()
file = open('textfile','r')
for line in file.readlines():
  if regexp2.search(line):
    count_regexp2 = count_regexp2 + 1
file.close()
file = open('textfile','r')
for line in file.readlines():
  if regexp3.search(line):
    count_regexp3 = count_regexp3 + 1
file.close()
file = open('textfile','r')
for line in file.readlines():
  if regexp4.search(line):
    count_regexp4 = count_regexp4 + 1
file.close()
print(f"{count_regexp=} {count_regexp2=} {count_regexp3=} {count_regexp4=}")