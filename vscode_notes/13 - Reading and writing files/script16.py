import shelve 
book = shelve.open('addresses')
print(book['flinstone'])
print(book['rubble'])