import os
with os.scandir("..") as my_file:
    for entry in my_file:
        print(entry,entry.is_file())
        print(entry,entry.is_dir())