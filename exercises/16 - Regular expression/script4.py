import re 
regexp = re.compile(r'\\ten')
f = open('textfile3','r')
count = 0 
for line in f.readlines():
    if regexp.search(line):
        count = count + 1
f.close()
print(count)