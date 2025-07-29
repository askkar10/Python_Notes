# multiple error argument
class MyError(Exception):
  pass

try: 
  raise MyError('some information','my_filename',3)
except MyError as error:
  print('Situation: {0} with file {1}\nerror code: {2}'.format(
      error.args[0],error.args[1],error.args[2]
  ))
