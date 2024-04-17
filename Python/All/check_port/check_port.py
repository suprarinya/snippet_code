import socket
import time
import sys
import threading
# pip install invoke
from invoke import run

host = '127.0.0.1'
port = 5000
camera_path = 'C:/allindex/capture/__pycache__/source0.cpython-310.pyc'
# get python.exe path
python_path = sys.executable

force_close = False

def port_check(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) #Timeout in case of port not open
    try:
        s.connect((host, port))
        return True
    except:
      return False

def run_cmd(python_path, camera_path):
    cmd = f"{python_path} {camera_path}"
    status = run(cmd, hide=None, warn=True)

while(True):
    is_port_open = port_check(host, port)

    t1 = threading.Thread(target=run_cmd, args=(python_path, camera_path))

    if is_port_open is False:
        try:
            if not t1.is_alive():
                t1.start()
        except Exception as e:
            pass

    time.sleep(5)


    

