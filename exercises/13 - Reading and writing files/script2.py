# a)

#f = open('ilosc_linii.txt','r')
#count = 0
#for l in f:
#    count += 1
#f.close()

#print(f"Ilość lini w tekście: {count}")


# b)
f = open('ilosc_linii.txt','r')
ilosc_linii = len(f.readlines())
print(f"Ilość linii w tekście to: {ilosc_linii}")

