import cv2
import zmq
from flask import Flask, render_template, Response
import numpy as np

# initialize the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.subscribe(b"")

# initialize the Flask app
app = Flask(__name__)

@app.route("/")
def index():
    # render the HTML template
    return render_template("index.html")

def generate():
    while True:
        # receive the encoded image over ZeroMQ
        encoded = socket.recv()

        # decode the encoded image into a NumPy array
        array = np.frombuffer(encoded, dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_COLOR)

        # convert the image to JPEG format
        _, jpeg = cv2.imencode(".jpg", image)

        # yield the JPEG image as a byte string
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

@app.route("/video_feed")
def video_feed():
    # return a response with the video stream
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    # run the Flask app
    app.run(debug=True)