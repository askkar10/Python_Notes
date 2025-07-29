# connecting to national oceanic and atmospheric administration ftp:

import ftplib
ftp = ftplib.FTP('tgftp.nws.noaa.gov')
ftp.login()

# change directiories nad list them
ftp.cwd('data')
print(ftp.nlst())

# fetching for example the latest METAR report for chicago o'hare international airport

import ftplib
ftp = ftp.retrbinary('RETR observations/metar/decoded/KORD.TXT',
                     open('KORD.TXT','wb').write)

x = open('KORD.TXT').readlines()
print(x)