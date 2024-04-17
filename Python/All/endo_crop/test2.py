import cv2
import os
import numpy as np

def contour_touches_border(contour, img_shape):
    img_h, img_w = img_shape[:2]
    return any((x <= 1 or y <= 1 or x >= img_w - 2 or y >= img_h - 2) for point in contour for x, y in [point[0]])

def filter_contours(contours, img_shape, min_contour_area):
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area and not contour_touches_border(cnt, img_shape)]
    return filtered_contours

def find_largest_contour(contours):
    if len(contours) != 0:
        largest_contour = max(contours, key=cv2.contourArea)
        return largest_contour
    else:
        return None

def process_image(file_path, min_contour_area=500*400):  # 500x400 is the minimum area
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    contours = filter_contours(contours, image.shape, min_contour_area)
    largest_contour = find_largest_contour(contours)
    
    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)
        if w < 1000 and h < 800:  # Ensuring the cropped area is not smaller than expected
            return None
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    else:
        return None
    
ori_path = "assets"
files = [f for f in os.listdir(ori_path) if os.path.isfile(os.path.join(ori_path, f))]

cropped_images = [process_image(os.path.join('assets', file_path)) for file_path in files]

# Checking and saving the cropped images
for idx, cropped_img in enumerate(cropped_images):
    print(cropped_images, idx)
    if cropped_img is not None:
        output_path = f'cropped/cropped_image_{idx}.jpg'
        cv2.imwrite(output_path, cropped_img)
        print(f'Cropped image saved to: {output_path}')
    else:
        print(f'No suitable contour found for image: {files[idx]}')
