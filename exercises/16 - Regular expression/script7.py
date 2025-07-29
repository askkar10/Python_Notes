import re
string = 'if the the problem is textual, use the the re module'
pattern = r'the the'
regexp = re.compile(pattern)
x = regexp.sub('the',string)
print(x)