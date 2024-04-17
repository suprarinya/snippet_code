import cv2
import os

drawing = False
rectangles = []
ix, iy = -1, -1

def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, img

    # if the left mouse is clicked record the starting (x, y) coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img2 = img.copy()
            cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.imshow('image', img2)

    # if the left mouse button was released, record the ending (x, y) coordinate
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangles.append((ix, iy, x, y))
        print(rectangles, (ix, iy, x, y))
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

image_path = "sample.jpg"
img = cv2.imread(image_path)
clone = img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback("image", draw_rect)


while True:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        img = cv2.imread(image_path)
    elif key == ord('c'):
        break

cv2.destroyAllWindows()

# olympus = [(492, 5, 1504, 867)]

print('Bounding boxes: ', rectangles)