from ftplib import FTP

f=FTP('speedtest.tele2.net','anonymous','anonymous') 
arch=f.nlst()
f.quit()
for file in arch:
    print(file)