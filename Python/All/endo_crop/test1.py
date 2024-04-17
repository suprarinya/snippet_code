import cv2
import numpy as np
import os

def contour_touches_border(contour, height, width):
    # check if any point of contour touches the image's border
    return any(
         x <= 1 or y <= 1 or x >= width - 2 or y >= height - 2
        for point in contour.reshape(-1, 2)
        for x, y in [point]
    )



def process_image(file_path, min_width=1000, min_contour_area=800):
    image = cv2.imread(file_path)

    # change to greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # edge detection - ini 50, 150
    edges = cv2.Canny(blurred,50, 150)
    # find contours from the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # filter contour that touch the image's border
    h, w = image.shape[:2]
    # contours = [cnt for cnt in contours if not contour_touches_border(cnt, h, w)]
    contours = [
        cnt for cnt in contours 
        if not contour_touches_border(cnt, h, w) and cv2.contourArea(cnt) > min_contour_area
    ]

    if contours:
        # find the largest contour by area
        largest_contour = max(contours, key=cv2.contourArea)
        # get the bounding box of largest contour
        x, y, width, height = cv2.boundingRect(largest_contour)
        
        # crop the image using bounding box
        print(y,y+height, x,x+width)
        # if width < min_width:
        #     return None
        # cropped_image = image[y:y+height, x:x+width]
        # cropped_image = cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
        for cnt in contours:
            x, y, width, height = cv2.boundingRect(cnt)
            cropped_image = cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
        return cropped_image
    else:
        # contour not found, return original image or None
        return None
    
ori_path = "assets"
files = [f for f in os.listdir(ori_path) if os.path.isfile(os.path.join(ori_path, f))]
# print(files)

for file_path in files:
    newfile_path = os.path.join(ori_path, file_path)
    only_name = os.path.splitext(file_path)[0]
    cropped_image = process_image(newfile_path)
    print(cropped_image is not None)
    if cropped_image is not None:
        cv2.imwrite(os.path.join('cropped', only_name+'cropped.jpg'), cropped_image)
