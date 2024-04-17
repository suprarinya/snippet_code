# pip install psutil
import psutil

total = int()
used  = int()
free  = int()

# หาไซส์ของ drive ทั้งหมดในเครื่อง

for disk in psutil.disk_partitions():
    if disk.fstype:
        total += int(psutil.disk_usage(disk.mountpoint).total)
        used  += int(psutil.disk_usage(disk.mountpoint).used)
        free  += int(psutil.disk_usage(disk.mountpoint).free)

print(f'''    
    TOTAL DISK SPACE : {round(total / (1024.0 ** 3), 2)} GiB
    USED DISK SPACE  : {round(used / (1024.0 ** 3), 2)} GiB
    FREE DISK SPACE  : {round(free / (1024.0 ** 3), 2)} GiB
''')

import win32api
test = win32api.GetVolumeInformation("E:")
print(test, test[0])