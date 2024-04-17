import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout , QHBoxLayout, QLabel, QPushButton, QFormLayout, QVBoxLayout, QProgressBar, QScrollArea, QComboBox, QGroupBox
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class Widget(QWidget):

    def __init__(self, parent= None):
        super(Widget, self).__init__()

        btn_new = QPushButton("Append new label")
        self.connect(btn_new, SIGNAL('clicked()'), self.add_new_label)

        #Container Widget       
        self.widget = QWidget()
        #Layout of Container Widget
        layout = QVBoxLayout(self)
        for _ in range(20):
            label = QLabel("test")
            layout.addWidget(label)
        self.widget.setLayout(layout)

        #Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.widget)

        #Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(btn_new)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

    def add_new_label(self):
        label = QLabel("new")
        self.widget.layout().addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Widget()
    dialog.show()

    app.exec_()