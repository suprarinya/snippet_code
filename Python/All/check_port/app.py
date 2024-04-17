from flask import Flask  
import socket

  
app = Flask(__name__) #creating the Flask class object   

host = '127.0.0.1'
port = 5001

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

@app.route('/') #decorator drfines the   
def home():  
    portcam = is_port_in_use(5000)
    print(portcam)
    return f'{host} : {port} is running and camera is {portcam}'
  
if __name__ =='__main__':  
    app.run(host=host, debug = True, port=port)  