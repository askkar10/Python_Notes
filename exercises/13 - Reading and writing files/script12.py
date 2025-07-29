import shelve
book = shelve.open('addresses')
book['ja'] = ('ulica/numer bloku/numer mieszkania','kod pocztowy','miasto')
book['ty'] = ('ulica/numer bloku/numer mieszkania','kod pocztowy','miasto')
