import pickle
f = open('pickle_pack','rb')
a = pickle.load(f)
b = pickle.load(f)
c = pickle.load(f)

print(a,b,c)
