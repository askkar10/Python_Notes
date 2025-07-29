from pathlib import Path
cur_path = Path()
new_path = cur_path.joinpath('12','sample_data')
# print(list(new_path.iterdir())) # wypisze cały path + pliki
print(list(new_path.iterdir()))
print(list(new_path.glob("*")))

# old_path = Path('12/sample_data/README.md.old')
# new_path2 = Path('12/sample_data/README.md')
# old_path.rename(new_path2) # zmiana nazwy pliku

# new_path3 = Path('12/sample_data/8.tmp')
# new_path3.unlink() # usuwanie pliku

# new_path4 = Path('12/sample_data/10')
# new_path4.mkdir(parents=True) # stworzenie folderu

new_path5 = Path('12/sample_data/10')
new_path5.rmdir() # usuniecie folderu