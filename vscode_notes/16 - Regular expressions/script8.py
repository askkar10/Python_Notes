import re 
int_string = "1 2 3 4 5"
def init_match_to_float(match_obj):
  return(match_obj.group('num') + ".0")
pattern = r"(?P<num>[0-9]+)"
regexp = re.compile(pattern)
regexp.sub(init_match_to_float, int_string)
print(int_string)