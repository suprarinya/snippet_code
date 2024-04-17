import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class WidgetOne(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        button = QPushButton("Switch to Widget Two")
        button.clicked.connect(self.switch_to_widget_two)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_to_widget_two(self):
        self.hide()
        widget_two.show()

class WidgetTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        layout = QVBoxLayout()
        button = QPushButton("Switch to Widget Three")
        button.clicked.connect(self.switch_to_widget_three)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_to_widget_three(self):
        self.hide()
        widget_three.show()

class WidgetThree(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        button = QPushButton("Switch to Widget One")
        button.clicked.connect(self.switch_to_widget_one)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_to_widget_one(self):
        self.hide()
        widget_one.show()

def main():
    app = QApplication(sys.argv)
    
    global widget_one, widget_two, widget_three
    
    widget_one = WidgetOne()
    widget_two = WidgetTwo()
    widget_three = WidgetThree()

    widget_one.show()
    
    app.exec_()

if __name__ == "__main__":
    main()
