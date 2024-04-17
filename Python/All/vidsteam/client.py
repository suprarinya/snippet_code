import threading
from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient
from vidstream import AudioSender, AudioReceiver
import time

# client - เสียงอย่างเดียว 
# รัน server.py ก่อน client.py!!!

client3 = ScreenShareClient('192.168.68.30', 8081)
sender =  AudioSender('192.168.68.30', 8082)

receiver = AudioReceiver('192.168.68.137', 3032)

def start_streaming():
    t3 = threading.Thread(target=client3.start_stream)
    t4 = threading.Thread(target=sender.start_stream)
    t6 = threading.Thread(target=receiver.start_server)
    t3.start()
    t4.start()
    t6.start()

def run_loop():
    while True:
        try:
            start_streaming()     
        except:
            pass
        else:
            time.sleep(10)
            pass
            # break

run_loop()

# receiver.stop_server()

