from ftplib import FTP

f=FTP('speedtest.tele2.net','anonymous','anonymous') 
arch=f.nlst()
f.quit()
with open ('arch.txt','w+') as txt:
    for file in arch:
        txt.writelines(f'{file}\n')