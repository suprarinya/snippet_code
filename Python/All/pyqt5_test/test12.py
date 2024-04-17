from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyMainWindow(QMainWindow):
    urlDataChanged = pyqtSignal(str, dict)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        button = QPushButton("Change URL with Data", self)
        layout.addWidget(button)
        button.clicked.connect(self.changeURLWithData)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.loadWebPage()
        
        # Connect the loadFinished signal to a slot to handle URL loading completion
        self.web_view.loadFinished.connect(self.onLoadFinished)
        self.urlDataChanged.connect(self.handleURLData)

    def loadWebPage(self):
        url = QUrl("http://localhost/playground")
        self.web_view.setUrl(url)

    def changeURLWithData(self):
        new_url = "http://localhost"  # Replace with the new URL
        data = {"key1": "value1", "key2": "value2"}  # Your data to send

        # Emit a custom signal with the new URL and data
        self.urlDataChanged.emit(new_url, data)

    def onLoadFinished(self):
        print('show')
        # Handle the widget visibility after the web page finishes loading
        self.web_view.show()  # Show the widget after the new URL is loaded

    def handleURLData(self, new_url, data):
        print(f"Received data: {data}")
        self.web_view.setUrl(QUrl(new_url))

def main():
    app = QApplication([])
    window = MyMainWindow()
    window.show()

    # Create an instance of MyMainWindow to access the signal
    instance = MyMainWindow()

    # Connect the signal to a slot that handles the URL and data
    # instance.urlDataChanged.connect(instance.handleURLData)

    app.exec_()

if __name__ == '__main__':
    main()
