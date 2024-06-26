# import the necessary packages
# 
from imutils.video import FileVideoStream
# 
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", required=True,
# 	help="blackpink.mp4")
# args = vars(ap.parse_args())
# open a pointer to the video stream and start the FPS timer
stream = cv2.VideoCapture('blackpink.mp4')

# start the file video stream thread and allow the buffer to
# start to fill
# print("[INFO] starting video file thread...")
# fvs = FileVideoStream('blackpink.mp4').start()
# time.sleep(1.0)

fps = FPS().start()

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video file stream
	(grabbed, frame) = stream.read()
	# if the frame was not grabbed, then we have reached the end
	# of the stream
	if not grabbed:
		break
	# resize the frame and convert it to grayscale (while still
	# retaining 3 channels)
	frame = imutils.resize(frame, width=450)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = np.dstack([frame, frame, frame])
	# display a piece of text to the frame (so we can benchmark
	# fairly against the fast method)
	cv2.putText(frame, "Slow Method", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
	# show the frame and update the FPS counter
	cv2.imshow("Frame", frame)
	cv2.waitKey(1)
	fps.update()

# loop over frames from the video file stream
# while fvs.more():
# 	# grab the frame from the threaded video file stream, resize
# 	# it, and convert it to grayscale (while still retaining 3
# 	# channels)
# 	frame = fvs.read()
# 	frame = imutils.resize(frame, width=450)
# 	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	frame = np.dstack([frame, frame, frame])
# 	# display the size of the queue on the frame
# 	cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
# 		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
# 	# show the frame and update the FPS counter
# 	cv2.imshow("Frame", frame)
# 	cv2.waitKey(1)
# 	fps.update()

# stop the timer and display FPS information
# fps.stop()
# print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# [INFO] elasped time: 75.50
# [INFO] approx. FPS: 61.61

# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()

# cv2.destroyAllWindows()
# fvs.stop()