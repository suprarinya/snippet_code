import os
import sys
from functions import *
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtGui import  QPixmap,QPainter, QFont
from PyQt5.QtCore import Qt
from ctypes import *

class LeftPart(QWidget):
    def __init__(self):
        super(LeftPart, self).__init__()
        self.setStyleSheet("background-color: #202020;") 
        self.setMaximumWidth(420)

        # self.img_count = 0
        
        self.layout = QVBoxLayout(self)

        self.imglabel = QLabel(' Images (0)', self)
        self.imglabel.setStyleSheet("color: white; font-size: 24px;") 
        self.imglabel.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.imglabel)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setMaximumWidth(500)
        
        self.layout.addWidget(self.scroll_area)

        self.scroll_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        self.scroll_layout = QVBoxLayout(self.scroll_widget)

    def add_image(self, image_path):
        is_file_exist = False
        attempt_check = 0
        while is_file_exist == False and attempt_check <= 5:
            is_file_exist = os.path.isfile(image_path)

        if is_file_exist == True:
            label = QLabel()
            label.setAlignment(Qt.AlignTop)

            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaledToWidth(300)
            try:
                self.draw_number(label, scaled_pixmap)
            except:
                pass
        else:
            pass

    def draw_number(self, label, scaled_pixmap):
        self.imglabel.setText(f"Images ({self.scroll_layout.count()+1})")

        image_count = self.count_pic()
        number_pixmap = QPixmap(scaled_pixmap)
        painter = QPainter(number_pixmap)
        painter.setPen(Qt.white)  
        painter.setFont(QFont("Arial", 24))  
        painter.drawText(150, 80, str(image_count))  
        painter.end()

        label.setPixmap(number_pixmap)
        self.scroll_layout.addWidget(label)

    def count_pic(self):
        return self.scroll_layout.count() + 1