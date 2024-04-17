import zmq
import cv2
import threading
import time
from flask import Flask, render_template, Response
import numpy as np

app = Flask(__name__)

# Initialize the ZMQ context
context = zmq.Context()

def send_video(room_name, cam_id, port):
    # Initialize the ZMQ publisher socket
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://*:{port}")

    cap = cv2.VideoCapture(cam_id)

    while True:
        ret, frame = cap.read()

        try:
            if ret:
                encoded = cv2.imencode(".jpg", frame)[1]
                socket.send(encoded)
                time.sleep(0.01)
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                time.sleep(0.01)
                continue
        except Exception as e:
            cap.release()
            socket.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<room_name>')
def room(room_name):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    
    if room_name == 'room1':
        socket.connect("tcp://localhost:5002")
    elif room_name == 'room2':
        socket.connect("tcp://localhost:5003")
    elif room_name == 'room3':
        socket.connect("tcp://localhost:5004")
    else:
        return "Invalid room name"
    
    socket.subscribe(b"")

    return Response(generate(socket), mimetype="multipart/x-mixed-replace; boundary=frame")

def generate(socket):
    
    while True:
        # receive the encoded image over ZeroMQ
        encoded = socket.recv()

        array = np.frombuffer(encoded, dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_COLOR)

        _, jpeg = cv2.imencode(".jpg", image)

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

def main():
    # Start a separate thread for each room
    threading.Thread(target=send_video, args=("room1", 'asset/small.mp4', 5002)).start()
    threading.Thread(target=send_video, args=("room2", 'asset/sample.mp4', 5003)).start()
    threading.Thread(target=send_video, args=("room3", 0, 5004)).start()


    # Start the Flask web server
    app.run(debug=True, port=5001)

if __name__ == '__main__':
    main()