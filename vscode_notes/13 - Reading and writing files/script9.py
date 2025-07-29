import sys
f = open('outfile2.txt','w')
print('A first line.\n','A second line.\n', file=f) # tworzenie pliku za pomocą printa
f.close()