import os
with os.scandir("12") as my_dir:
  for entry in my_dir:
    print(entry.name, entry.is_file())