# pip install python-imagesearch
# py -m pip install pyautogui
from python_imagesearch.imagesearch import imagesearch_loop
from PIL import Image
import socketio
import time
import pyautogui
import cv2
import array

servernode = 'localhost'
sio = socketio.Client()
while True:
    try:
        sio.connect('http://'+servernode+':3000')
        break
    except:
        time.sleep(1)

@sio.on('chat message')
def on_message(data):
    print(data)
    if data == 'locate':
        search_img()
    if 'size' in data:
        search_img()
    if 'zoom' in data or 'home' in data:
        button_name = 'click' if 'zoom' in data else 'home'
        screen = data.replace('change_zoom', '') if 'zoom' in data else data.replace('change_home', '')
        resolution = screen.split('x')
        width = resolution[0]
        ratio = resolution[1]
        new_name = f'{width}_{ratio}'
        # search_img(button=button_name,name=new_name)
        search_count(button=button_name,name=new_name)
        

def resize_img(width, height, img_name):
    try:
        image = Image.open(img_name)
        new_image = image.resize((width, height))
        new_image.save(img_name)
    except:
        print('can not open image')


def get_width_height(wh_str):
    exp = wh_str.split('x')

    data = []
    data['width'] = exp[0]
    data['height'] = exp[1]

    return data

def search_img(button='click', name=100):
    pos = imagesearch_loop(f"./button_{button}/button_{button}{name}.png", 1)
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0]+15, pos[1]+15)
    pyautogui.click()

def search_count(button='click', name=100):
    image_counted = f"./button_{button}/button_{button}{name}.png"
    search_img()


