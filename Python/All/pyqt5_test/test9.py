import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Click Me", self)
        button.setGeometry(100, 80, 100, 30)
        button.setObjectName("myButton")  # Set the object name for the button
        button.hide()
        # Connect a slot to the button's click event
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button clicked")

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()

    # Programmatically click the button
    button = window.findChild(QPushButton, "myButton")  # Find the button by its object name
    print(button)
    if button:
        button.click()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()