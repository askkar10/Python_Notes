def safe_apply(function,x,y):
  try:
    return function(x,y)
  except TypeError:
    return None
def dodawanie(x,y):
  return x + y
print(safe_apply(dodawanie,12,40)) 