# working/
#   item_info.txt
#   item_attributes.txt
#   related_items.txt
#   archive/
#     2024-09-15/
#       item_info.txt
#       item_attributes.txt
#       related_items.txt
#     2024-09-16/
#       item_info.txt
#       item_attributes.txt
#       related_items.txt     

import datetime
import pathlib

FILE_PATTERN = '*.txt'
ARCHIVE = 'archive'

def main():
  date_string = datetime.date.today().strftime('%Y-%m-%d')
  cur_path = pathlib.Path.cwd()
  archive_path = cur_path.joinpath(ARCHIVE)
  archive_path.mkdir(exist_ok=True)
  new_path = archive_path.joinpath(date_string)
  new_path.mkdir(exist_ok=True)
  paths = cur_path.glob(FILE_PATTERN)
  for path in paths:
    path.rename(new_path.joinpath(path.name))

if __name__ == "__main__":
  main()