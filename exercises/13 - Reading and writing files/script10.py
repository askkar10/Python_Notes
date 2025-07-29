import pickle 
a = 22; b = 3.14; c = 'test'
f = open('pickle_pack','wb')
pickle.dump(a,f)
pickle.dump(b,f)
pickle.dump(b,f)
f.close()