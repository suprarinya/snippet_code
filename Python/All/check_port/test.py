# import sys


# print(sys.executable)

# import os
# os.system("taskkill /im python.exe")

def is_port_in_use(port: int) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


port = is_port_in_use(5000)
print(port)