import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.widget1 = QWidget()
        self.widget2 = QWidget()
        
        layout = QVBoxLayout(self.central_widget)

        button1 = QPushButton("Show Widget 1", self)
        button1.clicked.connect(self.showWidget1)

        button2 = QPushButton("Show Widget 2", self)
        button2.clicked.connect(self.showWidget2)

        layout.addWidget(button1)
        layout.addWidget(button2)

    def showWidget1(self):
        self.widget1.show()
        self.widget2.hide()

    def showWidget2(self):
        self.widget1.hide()
        self.widget2.show()

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    
    # Initially, show Widget 1
    # window.showWidget1()

    window.show()

    button = window.findChild(QPushButton, "Show Widget 2")
    print(button)
    if button:
        button.click()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()