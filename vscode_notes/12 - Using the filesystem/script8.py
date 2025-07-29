import os
import glob
os.chdir('12/sample_data')
os.curdir # powinno wypisać wszystkie pliki w danym directory
print(glob.glob("*")) # wypisze wszystkie pliki
print(glob.glob("*.json")) # wypisze wszystki pliki json ktore sie tam znajduja
print(glob.glob("?.tmp")) # wypisze wszystkie pliki tmp
print(glob.glob("[0-9].tmp")) # wypisze tylko te ktore maja w nazwie tylko liczby od 0 do 9


# os.rename('README.md','README.md.old') # zmiana nazwy pliku

# os.remove('wiktoria.tmp') # usuwanie pliku
# os.makedirs('mydir') # stworzenie path folderu
# lub os.mkdir('anna.txt') 

# os.rmdir('mydir') # usniecie folderu



