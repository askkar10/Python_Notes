import ftplib
ftp = ftplib.FTP('tgftp.nws.noaa.gov')
ftp.login()
ftp.cwd('data')

# ftp = ftp.retrbinary('RETR observations/metar/decoded/KORD.TXT',
#                     open('KORD.TXT','wb').write)

x = open('KORD.txt','rb').readlines()
print(x)
