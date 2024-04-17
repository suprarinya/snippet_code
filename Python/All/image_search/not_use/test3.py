from python_imagesearch.imagesearch import imagesearch_loop, imagesearch_region_loop
import pyautogui
import time


# img_arr = ["./button_click100.png", "./button_home100.png"]
img_arr = "./button_home/button_home1920_100.png"
num = 0
while True:
    # pos = imagesearch_loop(img_arr[num], 1)
    pos = imagesearch_loop(img_arr, 1)
    print("position : ", pos[0], pos[1])

    pyautogui.moveTo(pos[0]+15, pos[1]+15)
    pyautogui.click()
    time.sleep(5)

    # num = 1 if num == 0 else 0

