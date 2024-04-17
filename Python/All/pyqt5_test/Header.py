import threading

import time
from functions import *
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from ctypes import *

disk_path = 'D:/'

QCAP = CDLL('D:/allindex/capture/QCAP.X64.DLL')
device0 = c_void_p(0)
QCAP_START_RECORD                       = CFUNCTYPE(c_ulong, c_void_p, c_uint, c_char_p,c_ulong, c_double, c_double, c_double, c_ulong, c_char_p)
PF_VIDEO_PREVIEW_CALLBACK               = CFUNCTYPE(c_ulong, c_void_p, c_double, c_void_p, c_ulong, c_void_p)
PF_AUDIO_PREVIEW_CALLBACK               = CFUNCTYPE(c_ulong, c_void_p, c_double, c_void_p, c_ulong, c_void_p)
PF_SIGNAL_REMOVED_CALLBACK              = CFUNCTYPE(c_ulong, c_void_p, c_long, c_long, c_void_p)
PF_FORMAT_CHANGED_CALLBACK              = CFUNCTYPE(c_ulong, c_void_p, c_ulong, c_ulong, c_ulong, c_ulong, c_int, c_double, c_ulong, c_ulong, c_ulong, c_void_p)
PF_NO_SIGNAL_DETECTED_CALLBACK          = CFUNCTYPE(c_ulong, c_void_p, c_long, c_long, c_void_p)
PF_WEBRTC_CHATROOM_LOGIN_CALLBACK_EX    = CFUNCTYPE(c_ulong, c_void_p, c_ulong, c_void_p, c_void_p)

class Header(QWidget):
    def render_time(self):
        starttime = time.time()
        while True:
            timestr = get_time_str()
            self.timelabel.setText(timestr)
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    def __init__(self):
        super(Header, self).__init__()
        # self.setStyleSheet("background-color: black;") 
        self.hglayout = QGridLayout()
        self.vlayout  = QVBoxLayout()

        self.imglabel = QLabel()
        self.img       = QPixmap('D:/allindex/recorder/asset/luminalogo.png')
        self.imglabel.setPixmap(self.img)
        self.imglabel.resize(self.img.width(), self.img.height())
        self.imglabel.setAlignment(Qt.AlignLeft)


        self.timelabel = QLabel('THU, 19 October, 2023 13:40:18 PM', self)
        self.timelabel.setStyleSheet("color: white; font-size: 24px;") 
        self.timelabel.setAlignment(Qt.AlignCenter)

        self.refresh = QPushButton('', self)
        self.refresh.clicked.connect(self.rescope)
        self.refresh.setIcon(QIcon('D:/allindex/recorder/asset/rescope.jpg'))
        self.refresh.setIconSize(QSize(50,50))

        total, used, free = read_drive(disk_path)
        used_percent = int((free * 100) / total) if total != 0 else 0

        self.disklabel = QLabel(f'{free} / {total} GB ({used_percent}%)', self)
        self.disklabel.setStyleSheet("color: white; font-size: 24px;") 
        self.disklabel.setAlignment(Qt.AlignLeft)

        self.pbar = QProgressBar(self)
        # self.pbar.setGeometry(10, 10, 20, 25) 
        self.pbar.setValue(used_percent)

        self.vlayout.addWidget(self.disklabel)
        self.vlayout.addWidget(self.pbar)

        self.tempwidget = QWidget()
        self.tempwidget.setLayout(self.vlayout)
        
        self.hglayout.addWidget(self.imglabel, 0, 0)   
        self.hglayout.addWidget(self.tempwidget, 0, 1)        
        self.hglayout.addWidget(self.timelabel, 0, 3, 2, 1)
        self.hglayout.addWidget(self.refresh, 0, 5)

        self.setLayout(self.hglayout)

        timethreading = threading.Thread(target=self.render_time)
        timethreading.start()

    def rescope(self):
        QCAP.QCAP_STOP(device0)
        QCAP.QCAP_DESTROY()
        camera = CameraScreen()
        start_camera(camera)

class CameraScreen(QWidget):
    def __init__(self):
        super(CameraScreen, self).__init__()
        start_camera(self)

def start_camera(self):
    print('start camera')
    self.m_bNoSignal = c_bool(False)
    self.m_pColorSpaceType = c_ulong(0)
    self.m_pWidth = c_ulong(0)
    self.m_pHeight = c_ulong(0)
    self.m_pIsInterleaved = c_bool(False)
    self.m_pFrameRate = c_double(0)
    self.m_pChannels = c_ulong(0)
    self.m_pBitsPerSample = c_ulong(0)
    self.m_pSampleFrequency = c_ulong(0)
    self.m_strFormatChangedOutput = "INFO..."
    self.chatroom = c_void_p(0)
    self.chatter = c_void_p(0)
    self.peerID = c_ulong(0)
    self.sender = c_void_p(0)
    self.bStreamEnabled = False

    def on_no_signal_detected(pDevice, nVideoInput, nAudioInput, pUserData):
        print("------------no signal detected callback----------------")
        m_bNoSignal = True
        return 0
    def on_signal_removed(pDevice, nVideoInput, nAudioInput, pUserData):
        print("------------signal removed callback----------------")
        m_bNoSignal = True
        return 0
    def on_format_changed(pDevice, nVideoInput, nAudioInput, nVideoWidth, nVideoHeight, bVideoIsInterleaved, dVideoFrameRate, nAudioChannels, nAudioBitsPerSample, nAudioSampleFrequency, pUserData):
        print("-on_process_format_changed (%d, %d, %d, %d, %d, %f, %d, %d, %d, %r)" % (nVideoInput, nAudioInput, nVideoWidth,nVideoHeight, bVideoIsInterleaved, dVideoFrameRate, nAudioChannels, nAudioBitsPerSample, nAudioSampleFrequency, pUserData))
        return 0
    def on_video_preview(pDevice, dSampleTime, pFrameBuffer, nFrameBufferLen, pUserData):
        if self.bStreamEnabled is True:
            QCAP.QCAP_SET_VIDEO_BROADCAST_SERVER_UNCOMPRESSION_BUFFER(self.sender, 0, self.m_pColorSpaceType, self.m_pWidth, self.m_pHeight, c_void_p(pFrameBuffer), c_ulong(nFrameBufferLen), c_double(0.0))
        return 0
    def on_audio_preview(pDevice, dSampleTime, pFrameBuffer, nFrameBufferLen, pUserData):
        if self.bStreamEnabled is True:
            QCAP.QCAP_SET_AUDIO_BROADCAST_SERVER_UNCOMPRESSION_BUFFER(self.sender, 0, c_void_p(pFrameBuffer), c_ulong(nFrameBufferLen), c_double(0.0))
        return 0
    def on_webrtc_chatroom_login(pChatRoom, nPeerID, pszPeerUserName, pUserData):
        if nPeerID != self.peerID:
            QCAP.QCAP_START_WEBRTC_CHAT(self.chatter, nPeerID)
        return 0
    def fun_timer():
        if self.m_bNoSignal == True:
            pass
        else:
            print(self.m_pWidth, self.m_pHeight)
            QCAP.QCAP_GET_VIDEO_CURRENT_INPUT_FORMAT(device0, byref(self.m_pColorSpaceType), byref(self.m_pWidth), byref(self.m_pHeight), byref(self.m_pIsInterleaved), byref(self.m_pFrameRate))
            QCAP.QCAP_GET_AUDIO_CURRENT_INPUT_FORMAT(device0, byref(self.m_pChannels), byref(self.m_pBitsPerSample), byref(self.m_pSampleFrequency))

    self.m_pNoSignalDetectedCB      = PF_NO_SIGNAL_DETECTED_CALLBACK(on_no_signal_detected)
    self.m_pSignalRemovedCB         = PF_SIGNAL_REMOVED_CALLBACK(on_signal_removed)
    self.m_pFormatChangedCB         = PF_FORMAT_CHANGED_CALLBACK(on_format_changed)
    self.m_pVideoPreviewCB          = PF_VIDEO_PREVIEW_CALLBACK(on_video_preview)
    self.m_pAudioPreviewCB          = PF_AUDIO_PREVIEW_CALLBACK(on_audio_preview)
    self.m_pWebrtcChatroomLoginCB   = PF_WEBRTC_CHATROOM_LOGIN_CALLBACK_EX(on_webrtc_chatroom_login)
    QCAP.QCAP_CREATE(vdo.strDevName.encode('utf-8'), 0,c_int64(int(self.winId())), byref(device0), 1, 0)
    QCAP.QCAP_REGISTER_FORMAT_CHANGED_CALLBACK(device0, self.m_pFormatChangedCB, None)
    QCAP.QCAP_REGISTER_NO_SIGNAL_DETECTED_CALLBACK(device0, self.m_pNoSignalDetectedCB, None)
    QCAP.QCAP_REGISTER_SIGNAL_REMOVED_CALLBACK(device0, self.m_pSignalRemovedCB, None)
    QCAP.QCAP_REGISTER_VIDEO_PREVIEW_CALLBACK(device0, self.m_pVideoPreviewCB, None)
    QCAP.QCAP_REGISTER_AUDIO_PREVIEW_CALLBACK(device0, self.m_pAudioPreviewCB, None)
    QCAP.QCAP_RUN(device0)
    timer = threading.Timer(1, fun_timer)
    timer.start()