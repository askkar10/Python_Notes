import re
regexp = re.compile(r'(?P<last>([-a-zA-Z]+)),'
                    r' (?P<first>([-a-zA-Z]+))'
                    r'( (?P<middle>([-a-zA-Z]+)))?'
                    r': (?P<phone>(\d{3}-)?\d{3}-\d{4})')

f = open('people','r')
for line in f.readlines():
    result = regexp.search(line)
    if result == None:
        print("Ten rekord nie pasuje!")
    else:
        first_name = result.group('first')
        last_name = result.group('last')
        middle_name = result.group('middle')
        if middle_name == None:
            middle_name = ''
        phone_number = result.group('phone')
        print(f'{first_name=} {middle_name=} {last_name=} {phone_number=}')

