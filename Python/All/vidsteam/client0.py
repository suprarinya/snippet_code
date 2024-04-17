import threading
from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient
from vidstream import AudioSender, AudioReceiver

# Choose One
# client1 = CameraClient('192.168.68.30', 8081)
# client2 = VideoClient('192.168.68.30', 8081, 'video.mp4')
client3 = ScreenShareClient('192.168.68.30', 8081)

#  client - sound only

# client - sender
sender =  AudioSender('192.168.68.30', 8082)
receiver = AudioReceiver('192.168.68.137', 3032)

def start_streaming():
    t3 = threading.Thread(target=client3.start_stream)
    t4 = threading.Thread(target=sender.start_stream)
    t6 = threading.Thread(target=receiver.start_server)
    t3.start()
    t4.start()
    t6.start()

start_streaming()


# client1.start_stream()
# client2.start_stream()
# client3.start_stream()
# sender.start_stream()