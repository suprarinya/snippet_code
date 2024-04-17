import os
import callfunction
import time
import vlc
import sys
from functions import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, pyqtSignal
from ctypes import *
import Header

# play sound
s_recstart = vlc.MediaPlayer(vdo.dirsound+"recording_start.mp3")
s_recstop  = vlc.MediaPlayer(vdo.dirsound+"recording_stop.mp3")

class RightPart(QWidget):
    update_signal = pyqtSignal(str)

    def __init__(self, leftpart):
        super(RightPart, self).__init__()
        self.setStyleSheet("background-color: black;") 

        self.leftpart = leftpart

        self.vlayout  = QVBoxLayout()

        self.capture = QPushButton('', self)
        self.capture.clicked.connect(self.capture_img)
        self.capture.setIcon(QIcon('D:/allindex/recorder/asset/capture.jpg'))
        self.capture.setIconSize(QSize(50,50))

        self.record_start = QPushButton('', self)
        self.record_start.clicked.connect(self.record_vdo)
        self.record_start.setIcon(QIcon('D:/allindex/recorder/asset/record.jpg'))
        self.record_start.setIconSize(QSize(50,50))

        self.record_stop = QPushButton('', self)
        self.record_stop.clicked.connect(self.stop_vdo)
        self.record_stop.setIcon(QIcon('D:/allindex/recorder/asset/record_stop.jpg'))
        self.record_stop.setIconSize(QSize(50,50))

        self.finish = QPushButton('FINISH', self)
        self.finish.clicked.connect(self.finish_cam)
        self.finish.setIconSize(QSize(50,50))

        self.setStyleSheet(f'''
        QPushButton {{
            color: white;
        }}''')

        self.vlayout.addWidget(self.capture)
        self.vlayout.addWidget(self.record_start)
        self.vlayout.addWidget(self.record_stop)
        self.vlayout.addWidget(self.finish)

        self.setLayout(self.vlayout)

        self.record_stop.hide()

    def add_image(self, image_path):
        self.update_signal.emit(image_path)

    def capture_img(self):
        picname       = callfunction.picturename(cid, hn, 'jpg')
        img_name      = "D:/laragon/htdocs/ScreenRecord/" + picname
        QCAP.QCAP_SNAPSHOT_JPG(device0, img_name.encode('utf-8'), 100, 1, 0)
        while not os.path.exists(img_name):
            time.sleep(0.1)
        playsound_thread('shutter.mp3')
        print(img_name)
        self.add_image(img_name)

    def record_vdo(self):
        playsound_thread('recording_start.mp3')
        self.record_stop.show()
        self.record_start.hide()
        vdopath     = callfunction.picturename(cid, hn, 'mp4')
        vdoname     = callfunction.get_new_path('D:\laragon\htdocs\store\pyqt5', vdopath) 
        print(vdoname)
        while not os.path.exists(vdoname):
            QCAP.QCAP_SET_VIDEO_RECORD_PROPERTY(device0, 3, 0, 0, 1, 8000, 6 * 1024 * 1024, 60, 0, 0, 0)
            QCAP.QCAP_SET_AUDIO_RECORD_PROPERTY(device0, 3, 0, 1)
            QCAP.QCAP_START_RECORD(device0, 3, vdoname.encode('utf-8'), 7, 0, 0, 0, 0, 0)

    def stop_vdo(self):
        playsound_thread('recording_stop.mp3')
        self.record_stop.hide()
        self.record_start.show()
        QCAP.QCAP_STOP_RECORD(device0, 3, 1, 0)

    def finish_cam(self):
        kill_process()