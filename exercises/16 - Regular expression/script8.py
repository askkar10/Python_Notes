import re
def func(match_object):
    return (match_object.group('num') + ".0")
int_string = '1 2 3 4 5'
pattern = r'(?P<num>[0-9]+)'
regexp = re.compile(pattern)
x = regexp.sub(func,int_string)
print(x)