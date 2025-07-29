# odzyskiwanie tych danych

import pickle 
file = open('state','rb')
a = pickle.load(file)
b = pickle.load(file)
c = pickle.load(file)
file.close()
print(f"{a=} {b=} {c=}")