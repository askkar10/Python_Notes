# ?P<name> grupowanie regexpow
# result.group()
import re
regexp = re.compile(r'(?P<last>([-a-zA-Z]+)),'
                    r' (?P<first>([-a-zA-Z]+))'
                    r'( (?P<middle>([-a-zA-Z]+)))?'
                    r': (?P<phone>((\d{3}-)?\d{3}-\d{4}))'
                    )
file = open('textfile3','r')
for line in file.readlines():
  result = regexp.search(line)
  if result == None:
    print("Ops i don't this this is a record")
  else:
    last_name = result.group('last')
    first_name = result.group('first')
    middle_name = result.group('middle')
    if middle_name == None:
      middle_name = ""
    phone_number = result.group('phone')
    print(f"{first_name=} {middle_name=} {last_name=} {phone_number=}")
file.close()
