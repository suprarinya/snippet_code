import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QFont

import socketio


sio     = socketio.Client()
while True:
    try:
        sio.connect('http://localhost:3000')
        break
    except:
        time.sleep(1)

@sio.on('chat message')
def on_message(data):
    if data == 'close_background':
        mainWindow.close()

class BackGroundMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Background')
        self.setStyleSheet("background-color: black;")
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BackGroundMainWindow()
    sys.exit(app.exec_())



