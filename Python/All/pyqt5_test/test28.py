
# importing libraries 
import cv2 
import numpy as np 
  
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('http://localhost/store/20231106122906/2023-11-06/vdo/654879a2925a667c0b0c9b13_01_20231106122906_23110612292141_1.mp4') 
  
# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 
  
# Read until video is completed 
while(cap.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True: 
    # Display the resulting frame 
        cv2.imshow('Frame', frame) 
          
    # Press Q on keyboard to exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
cap.release() 
  
# Closes all the frames 
cv2.destroyAllWindows() 