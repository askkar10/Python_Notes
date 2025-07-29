#f = open('tekst.txt','w')
#f.write('ala ma kota')
#f.close() 

# a)
#f = open('tekst.txt','r')
#d = f.readline()
#f.close()
#print(d)

# b)
#f = open('tekst.txt','w')
#f.write('Hello World!')
#f.close()

# c)
#f = open('tekst.txt','a')
#f.write('\nWitaj Świecei!')
#f.close()

# d)
f = open('tekst.txt','r')
d = f.readlines()
print(d)