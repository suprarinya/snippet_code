import sys
from PyQt5 import QtCore, QtWebChannel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.stacked_widget = QStackedWidget()

        # Create the widget with QWebEngineView
        self.widget1 = QWidget()
        web_view = QWebEngineView()
        web_view.setUrl(QtCore.QUrl('http://example.com'))  # Set your desired URL
        layout1 = QVBoxLayout(self.widget1)
        layout1.addWidget(web_view)
        self.stacked_widget.addWidget(self.widget1)

        # Create the second widget (normal widget)
        self.widget2 = QWidget()
        button2 = QPushButton('Switch to Web')
        button2.clicked.connect(self.showWidget1)
        layout2 = QVBoxLayout(self.widget2)
        layout1.addWidget(button2)
        self.stacked_widget.addWidget(self.widget2)

        # Initially show the widget with QWebEngineView
        self.stacked_widget.setCurrentWidget(self.widget1)

        layout.addWidget(self.stacked_widget)

    def showWidget1(self):
        self.stacked_widget.setCurrentWidget(self.widget2)

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
