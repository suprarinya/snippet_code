from vidstream import StreamingServer
from vidstream import AudioReceiver

server = StreamingServer('192.168.68.137', 8081)
server.start_server()

receiver = AudioReceiver('192.168.68.137', 8082)
receiver.start_server()

# Other Code

# When You Are Done
# server.stop_server()