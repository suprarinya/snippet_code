# pip install ftplib
from ftplib import FTP, error_perm
import os
import sys

# change HOSTNAME to connect to another computer
HOSTNAME = "192.168.68.98"
PORT     = 21
USERNAME = "user"
PASSWORD = "12345"

ftp_server = FTP(timeout=10)
ftp_server.connect(HOSTNAME, PORT)
ftp_server.login(USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

def placeFiles(ftp, oripath, destpath):
    # isUploadSuccess: bool = False
    for name in os.listdir(oripath):
        localpath = os.path.join(oripath, name)
        # retCode = ''
        if not (destpath == None or destpath.strip() == ""):
            try:
                ftp.mkd(destpath)
            except:
                pass

        try:
            ftp.cwd(destpath)
            with open(localpath, 'rb') as file:  
                print(name, file)
                retCode = ftp.storbinary(f'STOR {name}', file) 
        except OSError:     
            pass
        except error_perm:       
            print ( "Error: could not change to " + destpath )
            pass
            # sys.exit("Ending Application")


        print('upload file successfully!')
        
        # if retCode.startswith('226'):
        #     isUploadSuccess = True

        # return isUploadSuccess

# folder = 'store'
folder = 'D:\\laragon\\htdocs\\store\\@fortest'
destpath = "/store2" 
status = placeFiles(ftp_server, folder, destpath)
print(status)

ftp_server.quit()
