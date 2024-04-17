from vidstream import StreamingServer
from vidstream import AudioReceiver, AudioSender
import threading
import time

#  server - screen, sound

server = StreamingServer('192.168.68.30', 8081)
receiver = AudioReceiver('192.168.68.30', 8082)

sender = AudioSender('192.168.68.137', 3032)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t5 = threading.Thread(target=sender.start_stream)
    t1.start()
    t2.start()
    t5.start()


def run_loop():
    while True:
        try:
            start_listening()
        except:
            pass
        else:
            time.sleep(10)
            pass
            # break

run_loop()

# server.stop_server()
# receiver.stop_server()