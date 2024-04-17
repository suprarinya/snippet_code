import cv2
import zmq
import time

# initialize the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# initialize the OpenCV video capture device
# capture = cv2.VideoCapture(0)
# from video file
video = cv2.VideoCapture("small.mp4")

while True:
    # read a frame from the video capture device
    # ret, frame = capture.read()
    try:
        ret, frame = video.read()

        if ret:
            # encode the frame as a JPEG image
            encoded = cv2.imencode(".jpg", frame)[1]
            # print(encoded)

            # send the encoded image over ZeroMQ
            socket.send(encoded)
            time.sleep(0.01)
        else :
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            time.sleep(0.01)
            continue
            
            
    except Exception as e:
        print(e)
        video.release()
        socket.close()