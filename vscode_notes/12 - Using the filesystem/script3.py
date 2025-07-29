import os
print(os.path.join('bin','utils','disktools')) # tam stworzymy dany path
# print(os.path.join('mydir\\bin','utils\\disktools','chkdisk'))

path1 = os.path.join('mydir','bin')
path2 = os.path.join('utils','disktools','chdisk')
print(os.path.join(path1,path2))

print(os.path.split(os.path.join('some','directory','path'))) # wypisze osobno ostatnia scieżke

print(os.path.basename(os.path.join('some','directory','path.jpg'))) # wypisze osobno plik

print(os.path.splitext(os.path.join('some','directory','path.jpg'))) # wypisz tylko jaki jest to rodzaj pliku

print(os.path.expandvars('$HOME\\temp')) # wypisz od razu od glownego roota