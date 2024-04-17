from vidstream import AudioReceiver
from vidstream import AudioSender

import threading

receiver = AudioReceiver('192.168.68.137', 3032)
receiver_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('192.168.68.30', 8082)
sender_thread = threading.Thread(target=sender.start_stream)

receiver_thread.start()
# sender_thread.start()