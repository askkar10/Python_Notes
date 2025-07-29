# exception group => multiple exceptiion by by except*
message = ''
try:
  raise ExceptionGroup("Multiple exceptions",[TypeError(),FileNotFoundError(),ValueError()])
except* TypeError:
  message += f"Handling TypeError\n"
except* IOError:
  message += f"Handling IOError\n"
except* ValueError:
  message += f"Handling ValueError"
finally:
  print(message)