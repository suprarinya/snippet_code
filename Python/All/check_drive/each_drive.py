import os
import string
import shutil
from math import floor
import json
import socketio
import time
import sys

f = open("D:/laragon/htdocs/config/project/scope.txt", "r")
config = json.loads(f.read())

sio = socketio.Client()

while True:
    try:
        sio.connect('http://'+config['servernode']+':3000')
        break
    except:
        time.sleep(1)

drive = string.ascii_uppercase
valid_drives = []
all_drives   = []

# หาไซส์ในแต่ละ drive ในเครื่อง
def format_one_decimal(x):
    x = floor(x*10)/10
    return x

def check_drives(arr):
    for each_drive in drive:
        if os.path.exists(each_drive+":\\"):
            arr.append(each_drive+":\\")
    return arr

def get_drive_space(drive):
    data_dict = {}

    try:
        total, used, free = shutil.disk_usage(drive)
        data_dict['drive'] = drive
        data_dict['total'] = format_one_decimal(total / (2**30))
        data_dict['used']  = format_one_decimal(used  / (2**30))
        data_dict['free']  = format_one_decimal(free  / (2**30))
    except Exception as e:
        data_dict['drive'] = drive
        data_dict['total'] = e
        data_dict['used']  = e
        data_dict['free']  = e
    
    return data_dict

valid_drives = check_drives(valid_drives)

for drive in valid_drives:
    if 'c' not in drive.lower() and 'd' not in drive.lower(): 
        drive_dict = get_drive_space(drive)
        # print(drive_dict)
        all_drives.append(drive_dict)

# print(all_drives)

to_json = json.dumps(all_drives)
sio.emit('chat message', to_json)

print(to_json)

sys.exit()




