import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2hsv

import cv2

# def hex2rgb(h):
#     h = h.lstrip('#')
#     return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


# hexValues = ["#b4a795", "#e7e0d6", "#d7cfc8"]
# hsvValues = []
# for i in hexValues:
#     hsvValues.append(rgb2hsv(hex2rgb(i)))

# print(hsvValues)

h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))