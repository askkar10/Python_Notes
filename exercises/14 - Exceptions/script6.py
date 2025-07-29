class MyError(Exception):
    pass
filename = 'tekst.txt'
try:
    raise MyError('some information about error',filename)
except MyError as error:
    print(f"Information about error: ",error.args[0])
    print(f"Filename: ", error.args[1])