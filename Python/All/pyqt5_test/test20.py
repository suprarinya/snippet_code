from PyQt5 import QtCore, QtWebChannel
from PyQt5.QtWidgets import QCheckBox, QListWidgetItem, QListWidget, QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QProgressBar, QScrollArea, QStackedWidget
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon, QPainter, QFont, QImage
from PyQt5.QtCore import Qt, QSize, pyqtSignal, pyqtSlot, QObject, QTime, QTimer
from PyQt5.QtWebEngineWidgets import *
import sys

class FileListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File List with Progress Bars")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        checkbox1 = QCheckBox()
        ck_label = QLabel('Drive 1')
        ck_layout = QHBoxLayout()
        ck_layout.addWidget(checkbox1)
        ck_layout.addWidget(ck_label)
        ck_layout.addStretch(1)
        temp2 = QWidget()
        temp2.setLayout(ck_layout)
        layout.addWidget(temp2)

        self.file_list = QListWidget()
        self.file_list.setVerticalScrollBarPolicy(0)  # Qt.ScrollBarAlwaysOff
        self.file_list.setHorizontalScrollBarPolicy(0)  # Qt.ScrollBarAlwaysOff
        layout.addWidget(self.file_list)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(1000)

        self.files = ["File1.txt", "File2.txt", "File3.txt"]
        self.progress_values = [0, 25, 50]

        for file, progress_value in zip(self.files, self.progress_values):
            custom_widget = FileWidgetItem(file, progress_value)
            item = QListWidgetItem(self.file_list)
            item.setSizeHint(custom_widget.sizeHint())
            self.file_list.setItemWidget(item, custom_widget)

        self.setLayout(layout)


    def updateProgress(self):
        for i in range(self.file_list.count()):
            custom_widget = self.file_list.itemWidget(self.file_list.item(i))
            custom_widget.updateProgress()

    
class FileWidgetItem(QWidget):
    def __init__(self, file, initial_progress):
        super().__init__()

        hlayout = QHBoxLayout()
        self.item_label = QLabel(f"File: {file}")
        hlayout.addWidget(self.item_label)

        self.progress = QProgressBar()
        self.progress.setValue(initial_progress)
        self.progress.setFormat(f"{initial_progress}%")
        hlayout.addWidget(self.progress)

        self.setLayout(hlayout)

    def updateProgress(self):
        current_value = self.progress.value()
        new_value = (current_value + 10) % 100  # Update the progress value
        self.progress.setValue(new_value)
        self.progress.setFormat(f"{new_value}%")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setFixedWidth(self.refresh_button.fontMetrics().width("Refresh")+30)
        refresh_layout = QHBoxLayout()
        refresh_layout.addStretch(1)
        refresh_layout.addWidget(self.refresh_button)
        temp1 = QWidget()
        temp1.setLayout(refresh_layout)

        # file_list_widget1 = FileListWidget()
        # file_list_widget2 = FileListWidget()
        self.filelist_layout = QVBoxLayout()
        file_list_widget1 = FileListWidget()
        file_list_widget2 = FileListWidget()
        self.filelist_layout.addWidget(file_list_widget1)
        self.filelist_layout.addWidget(file_list_widget2)
        layout_temp = QWidget()
        layout_temp.setLayout(self.filelist_layout)

        buttons_layout = QHBoxLayout()
        cancel_button = QPushButton("Cancel")
        confirm_button = QPushButton("Confirm")
        buttons_layout.addStretch(1)
        buttons_layout.addWidget(cancel_button)
        buttons_layout.addWidget(confirm_button)
        temp = QWidget()
        temp.setLayout(buttons_layout)

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(temp1)
        central_layout.addWidget(layout_temp)
        # central_layout.addWidget(file_list_widget1)
        # central_layout.addWidget(file_list_widget2)
        central_layout.addWidget(temp)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.refresh_button.clicked.connect(self.refreshList)

    def refreshList(self):
        # Implement your refresh logic here
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
