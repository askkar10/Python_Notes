import re
regexp = re.compile('hello')
f = open('textfile','r')
count = 0
for line in f.readlines():
    if regexp.search(line):
        count = count + 1
f.close()
print(count)