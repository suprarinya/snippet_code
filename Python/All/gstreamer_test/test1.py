# This script copies the video frame by frame
import cv2
import subprocess as sp

input_file = 'blackpink.mp4'
output_file = 'out.mp4'

cap = cv2.VideoCapture(input_file)
ret, frame = cap.read()
height, width, ch = frame.shape

ffmpeg = 'FFMPEG'
dimension = '{}x{}'.format(width, height)
f_format = 'bgr24' # remember OpenCV uses bgr format
fps = str(cap.get(cv2.CAP_PROP_FPS))

command = [ffmpeg,
        '-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-s', dimension,
        '-pix_fmt', 'bgr24',
        '-r', fps,
        '-i', '-',
        '-an',
        '-vcodec', 'mpeg4',
        '-b:v', '1000k',
        output_file ]

proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    proc.stdin.write(frame.tobytes())

cap.release()
proc.stdin.close()
proc.stderr.close()
proc.wait()