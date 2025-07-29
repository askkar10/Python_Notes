import fileinput
for line in fileinput.input(files='sole1.txt'):
    print(line,end='')