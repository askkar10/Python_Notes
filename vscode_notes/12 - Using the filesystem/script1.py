import os 
print(os.getcwd()) # wypisze w jakim folderze aktualnie pracujemy
print(os.listdir(os.curdir))
os.chdir('12') # przejśćie do danego folderu
print(os.getcwd())
print(os.listdir(os.curdir))