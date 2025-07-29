import re
regexp = re.compile(r'[-a-zA-Z]+,'
                    r' [-a-zA-Z]+'
                    r'( [-a-zA-Z]+)?'
                    r': (\d{3}-)?\d{3}-\d{4}'
                    )
f = open('people','r')
for line in f.readlines():
    if regexp.search(line):
        print("Tak znalazlem!!!")
f.close()