# connecting to national oceanic and atmospheric administration ftp:

import ftplib
ftp = ftplib.FTP('tgftp.nws.noaa.gov')
ftp.login()

# change directiories nad list them
ftp.cwd('data')
print(ftp.nlst())
