import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel

def get_progress_percent(orifile, newfile):
    # Your logic to calculate the progress percentage
    return 50  # Replace with your actual calculation

class BackgroundWorker(QThread):
    update_signal = pyqtSignal(int, str, str)

    def __init__(self, orifile, newfile, filename, drivename):
        super().__init__()
        self.orifile = orifile
        self.newfile = newfile
        self.filename = filename
        self.drivename = drivename

    def run(self):
        starttime = time.time()
        percent = 0
        while percent < 100:
            percent = get_progress_percent(self.orifile, self.newfile)
            self.update_signal.emit(percent, self.drivename, self.filename)
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))

class MainWidget(QWidget):
    def __init__(self, orifile, newfile, filename, drivename):
        super(MainWidget, self).__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Progress: 0%")
        layout.addWidget(self.label)

        self.worker = BackgroundWorker(orifile, newfile, filename, drivename)
        self.worker.update_signal.connect(self.update_progress)

        start_button = QPushButton("Start Background Task")
        start_button.clicked.connect(self.start_background_task)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_background_task(self):
        self.worker.start()

    def update_progress(self, percent, drivename, filename):
        self.label.setText(f"Progress: {percent}% - Drive: {drivename} - File: {filename}")

def main(orifile, newfile, filename, drivename):
    app = QApplication(sys.argv)
    window = QMainWindow()
    widget = MainWidget(orifile, newfile, filename, drivename)
    window.setCentralWidget(widget)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Replace these values with your actual file paths and names
    orifile = "D://laragon/htdocs/store/20231107103914/2023-11-07/vdo/6549b163ab839221b30d0756_01_20231107103914_23110710591950_1.mp4"
    newfile = "E://LuminaCapture//20231107103914//2023-11-07//video//aaa.mp4"
    filename = "6549b163ab839221b30d0756_01_20231107103914_23110710591950_1.mp4"
    drivename = "E://"
    main(orifile, newfile, filename, drivename)
