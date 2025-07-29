import re
regexp = re.compile(r'hello')
count = 0
file = open('textfile','r')
for line in file.readlines():
  if regexp.search(line):
    count = count + 1
file.close()
print(count)