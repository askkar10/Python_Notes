from datetime import datetime,timedelta
import pathlib
import zipfile

FILE_PATTERN = "*.zip"
ARCHIVE = 'archive'
ARCHIVE_WEEKDAY = 1

def main():
  cur_path = pathlib.Path.cwd()
  zip_file_path = cur_path.joinpath(ARCHIVE)
  paths = zip_file_path.glob(FILE_PATTERN)
  current_date = datetime.today()
  for path in paths:
    name = path.stem
    path_date = datetime.strptime(name,
                                  "%Y-%m-%d")
    path_timedelta = current_date - path_date
    if (path_timedelta > timedelta(days=30) and
    path_date.weekday() != ARCHIVE_WEEKDAY):
      path.unlink()
  
if __name__ == '__main__':
  main()