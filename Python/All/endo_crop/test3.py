import cv2
import numpy as np

def process_image(file_path, min_contour_area=800, central_bias=True):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # If central bias is True, modify contour choice logic
    if central_bias:
        # Get image central point
        h, w = image.shape[:2]
        center = (w // 2, h // 2)
        
        # Sort contours based on distance to center and area
        def contour_score(cnt):
            M = cv2.moments(cnt)
            # Avoid division by zero
            cX = int(M["m10"] / M["m00"]) if M["m00"] else center[0]
            cY = int(M["m01"] / M["m00"]) if M["m00"] else center[1]
            distance_to_center = np.sqrt((center[0] - cX) ** 2 + (center[1] - cY) ** 2)
            return distance_to_center - cv2.contourArea(cnt)

        contours = sorted(contours, key=contour_score, reverse=True)
    
    for cnt in contours:
        if cv2.contourArea(cnt) > min_contour_area:
            x, y, width, height = cv2.boundingRect(cnt)
            # If contour is a central one, draw it
            if central_bias:
                distance_to_center = np.sqrt(((x + width // 2) - center[0]) ** 2 + ((y + height // 2) - center[1]) ** 2)
                if distance_to_center < (w // 4):  # Arbitrary threshold for "centrality"
                    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
                    # Assume we only want the first central large contour
                    break
            else:
                cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    
    return image

# Replace 'path_to_your_image' with the path to your actual image
annotated_image = process_image('assets/416_17_506086_20211103110338_100.jpg')
# Replace 'path_to_save_annotated_image' with the actual path to save the annotated image
cv2.imwrite('1.jpg', annotated_image)
