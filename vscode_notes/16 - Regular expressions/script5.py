import re 
regexp = re.compile(r'[-a-zA-Z]+,'
                    r' [-a-zA-Z]+'
                    r'( [-a-zA-Z]+)?'
                    r': (\d{3}-)?\d{3}-\d{4}'
                    )
file = open("textfile3",'r')
for line in file.readlines():
  if regexp.search(line):
    print('Yeah i found so what')
  file.close()
