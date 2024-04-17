import sys
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEngineProfile

class FirstWidget(QWidget):
    urlChanged = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button = QPushButton("Change URL in Second Widget", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.changeURL)

        self.setLayout(layout)

    def changeURL(self):
        new_url = "http://www.localhost/endoindex"  # Replace with the new URL
        self.urlChanged.emit(new_url)  # Emit a signal with the new URL

class SecondWidget(QWebEngineView):
    urlChanged = pyqtSignal(str)  # Signal to notify the URL change

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        # self.settings().setAttribute(QWebEngineSettings.LocalStorageDatabaseEnabled, True)
        # self.settings().setAttribute(QWebEngineSettings.OfflineStorageDatabaseEnabled, True)
        # self.settings().setAttribute(QWebEngineSettings.OfflineWebApplicationCacheEnabled, True)
        # self.page().profile().setHttpUserAgent("Custom User Agent")
        # self.page().profile().clearHttpCache()
        # self.page().profile().setHttpCacheType(QWebEngineSettings.LocalStorage)
        # self.page().profile().httpCache().setMaximumSize(10 * 1024 * 1024)  # 10 MB cache size

        self.load(QUrl("http://www.localhost"))  # Initial URL

        # Connect the signal to the slot to handle URL changes
        self.urlChanged.connect(self.setNewURL)

    def setNewURL(self, new_url):
        self.load(QUrl(new_url))  # Load the new URL

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    # Create instances of the widgets
    first_widget = FirstWidget()
    second_widget = SecondWidget()

    # Connect the signal from the first widget to the slot in the second widget
    first_widget.urlChanged.connect(second_widget.urlChanged)

    layout = QVBoxLayout()
    layout.addWidget(first_widget)
    layout.addWidget(second_widget)
    central_widget.setLayout(layout)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
