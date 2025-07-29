# working/
#     item_info.txt
#     item_attributes.txt
#     related_items.txt
#     archive/
#         item_info_2024-09-15.txt
#         item_attributes_2024-09-15.txt
#         related_items_2024-09-15.txt
#         ...

import pathlib
import datetime

FILE_PATTERN = '*.txt'
ARCHIVE = 'archive'

def main():
  date_string = datetime.date.today().strftime("%Y-%m-%d")
  cur_path = pathlib.Path.cwd()
  archive_path = cur_path.joinpath(ARCHIVE)
  archive_path.mkdir(exist_ok=True)
  paths = cur_path.glob(FILE_PATTERN)
  for path in paths:
    new_filename = f"{path.stem}_{date_string}{path.suffix}"
    new_path = archive_path.joinpath(new_filename)
    path.rename(new_path)

if __name__ == '__main__':
  main()