import cv2
import numpy as np
import os

def detect_gi_region(file_path, min_contour=pow(10,5)):
    image = cv2.imread(file_path)

    # convert to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define hsv range (hue, sat, vol)
    lower_val = np.array([0, 0, 25])
    upper_val = np.array([175, 255, 255])

    # set color range 
    mask = cv2.inRange(hsv, lower_val, upper_val)

    #  clean up mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # find contours from mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # filter contour -> may need to
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour]

    # draw/crop largest contour
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # crop image
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image

        # draw rect : red for cropped, green for detect other contours
        color_rect = (0, 255, 0)
        for cnt in contours:
            x, y, width, height = cv2.boundingRect(cnt)
            if cnt is largest_contour:
                cropped_image = cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2)
            else:
                cropped_image = cv2.rectangle(image, (x, y), (x + width, y + height), color_rect, 2)
        return cropped_image
    
    else:
        return image  
    
def folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

ori_path = "assets"
dest_path = "cropped"
folder_exists(ori_path)
folder_exists(dest_path)
files = [f for f in os.listdir(ori_path) if os.path.isfile(os.path.join(ori_path, f))]
# print(files)

min_contour_area = pow(10, 5)

for file_path in files:
    newfile_path = os.path.join(ori_path, file_path)
    only_name = os.path.splitext(file_path)[0]
    cropped_image = detect_gi_region(newfile_path, min_contour_area)
    if cropped_image is not None:
        cv2.imwrite(os.path.join(dest_path, only_name+'cropped.jpg'), cropped_image)
