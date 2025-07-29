import shelve
book = shelve.open('addresses')
print(dict(book))