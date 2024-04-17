
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch_region_loop, imagesearch_count, imagesearcharea
from PIL import Image
import socketio
import time
import pyautogui
import cv2
import array

def search_img(button='click', name=100):
    pos = imagesearch_loop("D:/laragon/htdocs/playground/python/img_search/1484-100-1.png", 1)
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0]+15, pos[1]+15)
    pyautogui.click()

def search_img_top(button='click', name=100):
    # pos = imagesearch_region_loop("D:/laragon/htdocs/playground/python/img_search/1484-100-1.png", 1, 0, 0, 600, 450)
    file = 'D:/laragon/htdocs/playground/python/img_search/1484-100-2.png'
    pos = imagesearcharea(file, 0, 0, 800, 600)
    print("position top : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0]+15, pos[1]+15)
    # pyautogui.click()

def search_img_bottom(button='click', name=100):
    pos = imagesearch_region_loop("D:/laragon/htdocs/playground/python/img_search/1484-100-1.png", 1, 600, 600, 800, 800)
    print("position btm: ", pos[0], pos[1])
    pyautogui.moveTo(pos[0]+15, pos[1]+15)
    # pyautogui.click()

def search_count():
    pos = imagesearch_count("D:/laragon/htdocs/playground/python/img_search/1484-100-1.png")
    print('count', pos )

def search_img_bt():
        file = 'D:/laragon/htdocs/playground/python/img_search/1484-100-2.png'
        # pos = imagesearch_loop(file, 1)
        # pos = imagesearch_region_loop(file, 1, 0, 0, 600, 450)
        pos = imagesearcharea(file, 0, 0, 1400, 1400)
        arr2 = {}
        arr2['x'] = pos[0]
        arr2['y'] = pos[1]
        print('count', pos )
        pyautogui.moveTo(pos[0], pos[1]+60)

        return arr2 



while True:
    search_img_bt()
    time.sleep(3)
    search_img_top()
    time.sleep(3)
    # search_count()
    # search_img_bottom()