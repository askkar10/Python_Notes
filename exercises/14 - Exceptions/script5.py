class MyError(Exception):
    pass

try: 
    raise MyError('some information about error')
except MyError as error:
    print('Information: ',error)
