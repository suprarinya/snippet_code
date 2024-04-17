import os.path, os
import sys
import signal
from ftplib import FTP, error_perm

hn      = sys.argv[1]
host    = '172.28.131.81'
port    = 6000

def placeFiles(ftp,path):

    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            if name not in ftp.nlst():
                # print(ftp.nlst()[0])
                print("STOR", name, localpath)
                with open(localpath, 'rb') as file2:
                    ftp.storbinary('STOR ' + name, file2)
                    pass

        elif os.path.isdir(localpath):
            print("MKD", name)
            try:
                ftp.mkd(name)
            # ignore "directory already exists"
            except error_perm as e:
                if not e.args[0].startswith('550'): 
                    raise

            print("CWD", name)
            ftp.cwd(name)
            placeFiles(ftp, localpath)           
            print("CWD", "..")
            ftp.cwd("..")

ftp = FTP()
ftp.connect(host,port)
ftp.login('user','12345')
ftp.encoding = "utf-8"
filenameCV = "D:\\laragon\\htdocs\\store\\"+hn

# status = placeFiles(ftp_server, folder, destpath)
try:
    ftp.mkd("store\\"+hn)
except:
    pass

ftp.cwd("store\\"+hn)

placeFiles(ftp, filenameCV)

quit()
ftp.quit()
