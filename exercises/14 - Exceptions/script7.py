message = ''
try:
    raise ExceptionGroup('Multiple Exception',[TypeError(),FileNotFoundError(),ValueError()])
except* TypeError:
    message += "Handling TypeError()\n"
except* FileNotFoundError:
    message += "Handling FileNotFoundError()\n"
except* ValueError:
    message += "Handling ValueError()"
finally:
    print(message)