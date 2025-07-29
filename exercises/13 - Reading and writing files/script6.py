import sys
f = open('outfile.txt','w')
old_sys = sys.stdout
sys.stdout = f
sys.stdout.writelines(['Pierwsza linia tekstu','druga linia tekstu'])
print('Trzecia linia tekstu')
sys.stdout = old_sys
f.close()

