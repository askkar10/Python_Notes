import ftplib
ftp = ftplib.FTP('tgftp.nws.noaa.gov')
ftp.login()
ftp.cwd('data')
print(ftp.nlst())