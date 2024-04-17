# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QProgressBar, QListWidgetItem, QLabel
# from PyQt5.QtCore import QTimer

# class FileListWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("File List with Progress Bars")
#         self.setGeometry(100, 100, 400, 300)

#         layout = QVBoxLayout()

#         self.file_list = QListWidget()
#         layout.addWidget(self.file_list)

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.updateProgress)
#         self.timer.start(1000)

#         self.files = ["File1.txt", "File2.txt", "File3.txt"]
#         self.progress_values = [0, 25, 50]

#         for file, progress_value in zip(self.files, self.progress_values):
#             item = QListWidgetItem(file)
#             progress = QProgressBar()
#             progress.setValue(progress_value)
#             progress.setFormat(f"{progress_value}%")
#             self.file_list.addItem(item)
#             self.file_list.setItemWidget(item, progress)

#         self.setLayout(layout)

#     def updateProgress(self):
#         for i in range(self.file_list.count()):
#             item = self.file_list.item(i)
#             progress = self.file_list.itemWidget(item)
#             current_value = progress.value()
#             new_value = (current_value + 10) % 100  # Update the progress value
#             progress.setValue(new_value)
#             progress.setFormat(f"{new_value}%")

# def main():
#     app = QApplication(sys.argv)
#     window = FileListWidget()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QProgressBar, QListWidgetItem, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer

class FileListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File List with Progress Bars")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setFixedWidth(self.refresh_button.fontMetrics().width("Refresh"))
        refresh_layout = QHBoxLayout()
        refresh_layout.addStretch(1)
        refresh_layout.addWidget(self.refresh_button)
        layout.addLayout(refresh_layout)

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(1000)

        self.files = ["File1.txt", "File2.txt", "File3.txt"]
        self.progress_values = [0, 25, 50]

        for file, progress_value in zip(self.files, self.progress_values):
            item = QListWidgetItem(file)
            hlayout = QHBoxLayout()
            item_label = QLabel(f"File: {file}")
            hlayout.addWidget(item_label)
            # self.file_list.addItem(item)
            # self.file_list.setItemWidget(item, item_label)
            progress = QProgressBar()

            progress.setValue(progress_value)
            progress.setFormat(f"{progress_value}%")
            hlayout.addWidget(progress)

            temp = QWidget()
            temp.setLayout(hlayout)


            self.file_list.setItemWidget(item, temp)

        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.refresh_button.clicked.connect(self.refreshList)

    def updateProgress(self):
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            progress = self.file_list.itemWidget(item)
            current_value = progress.value()
            new_value = (current_value + 10) % 100  # Update the progress value
            progress.setValue(new_value)
            progress.setFormat(f"{new_value}%")

    def refreshList(self):
        # Implement your refresh logic here
        pass

def main():
    app = QApplication(sys.argv)
    window = FileListWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
