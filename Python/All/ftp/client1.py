# pip install ftplib
from ftplib import FTP, error_perm
import os

# Change these settings to match your FTP server
HOSTNAME = "192.168.68.15"
PORT = 2121
USERNAME = "user"
PASSWORD = "12345"

ftp_server = FTP(timeout=10)
ftp_server.connect(HOSTNAME, PORT)
ftp_server.login(USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

def uploadThis(path, destpath):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        if os.path.isfile(path + r'\{}'.format(f)):
            fh = open(f, 'rb')
            ftp_server.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(path + r'\{}'.format(f)):
            ftp_server.mkd(f)
            ftp_server.cwd(f)
            uploadThis(path + r'\{}'.format(f))
    ftp_server.cwd('..')
    os.chdir('..')
folder = 'store2'
destpath = "/store3" 
# placeFiles(ftp_server, folder, destpath)

uploadThis(folder, destpath) # now call the recursive function         


ftp_server.quit()
