kolory = ['czerwony','niebieski','zolty']
kolory[len(kolory):] = [1,2,3]
print(kolory,len(kolory))
nowe = [100,200]
kolory[:0] = nowe
print(kolory)

