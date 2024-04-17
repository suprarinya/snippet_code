import numpy as np
import cv2

image_shape = (883, 1570)
# Bounding box coordinates (x, y, width, height)
bounding_boxes = [(492, 5, 1504, 867)]

# Create an empty mask with the same dimensions as the image, filled with zeros (black)
mask = np.zeros(image_shape, dtype=np.uint8)

# Fill the area of the bounding box with ones (white)
for x, y, w, h in bounding_boxes:
    mask[y:y+h, x:x+w] = 1

# save the mask as an image file -  multiply 255 to amke the mask visible as an image
cv2.imwrite('mask.jpg', mask * 255)

cv2.imshow('Mask', mask * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

