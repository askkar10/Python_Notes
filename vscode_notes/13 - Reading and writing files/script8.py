import sys
f = open('outfile.txt','w')
old_sys_stdout = sys.stdout # przekierowanie
sys.stdout = f # zapisanie
sys.stdout.writelines(['A first line.\n','A second line.\n']) # wypisywanie to co ma zostac napisane do pliku
print('A line from the print function') # tutak tak samoe
sys.stdout = old_sys_stdout # przywrócenie poprzedniego stanu
f.close()