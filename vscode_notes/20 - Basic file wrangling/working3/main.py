# working/
#   archive/
#     2025-09-15.zip
#     2025-09.16.zip
#     2025-09-17.zip
#     ...

import datetime
import pathlib 
import zipfile

FILE_PATTERN = '*.txt'
ARCHIVE = 'archive'

def main():
  date_string = datetime.date.today().strftime("%Y-%m-%d")
  cur_path = pathlib.Path.cwd()
  archive_path = cur_path.joinpath(ARCHIVE)
  archive_path.mkdir(exist_ok=True)
  paths = cur_path.glob(FILE_PATTERN)
  zip_file_path = cur_path.joinpath(ARCHIVE,date_string+'.zip')
  zip_file = zipfile.ZipFile(str(zip_file_path),"w")
  for path in paths:
    zip_file.write(str(path))
    path.unlink()

if __name__ == '__main__':
  main()
