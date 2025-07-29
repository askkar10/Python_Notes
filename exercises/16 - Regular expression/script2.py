import re
regexp = re.compile('hello|Hello')
# regexp = re.compile('(h|H)ello')
# regexp = re.compile('[h|H]ello')
count = 0
f = open('textfile2','r')
for line in f.readlines():
    if regexp.search(line):
        count = count + 1
f.close()
print(count)