import re
regexp = re.compile('\\\\ten') # ('\\ten') nie zadziała, trzeba użyć czterech \\\\
count = 0
file = open('textfile2','r')
for line in file.readlines():
  if regexp.search(line):
    count = count + 1
file.close()
print(count)