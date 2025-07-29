from pathlib import Path
cur_path = Path()
print(cur_path.joinpath('bin','utils','disktools'))
print(cur_path / 'bin' / 'utils' / 'disktools')

a_path = Path('bin/utils/disktools')
print(a_path.parts) # wypisuje path w tuple

a_path = Path('some','directory','path.jpg')
print(a_path.name) # zwraca tylko base name
print(a_path.parent) # zwraca tylko te foldery nad basename
print(a_path.suffix) # zwraca tylko rodzaj pliku