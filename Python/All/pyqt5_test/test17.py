import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt

class ModalDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modal Dialog")
        self.setGeometry(100, 100, 400, 200)
        self.setWindowModality(2)  # Make it modal

        layout = QVBoxLayout()

        # Content of the modal
        label = QLabel("This is a modal dialog with a black background.")
        layout.addWidget(label)

        # Buttons
        button_layout = QHBoxLayout()
        confirm_button = QPushButton("Confirm")
        confirm_button.setStyleSheet("background-color: blue;")  # Black background
        confirm_button.clicked.connect(self.confirm)
        close_button = QPushButton("Close")
        close_button.setStyleSheet("background-color: blue;")  # Black background
        close_button.clicked.connect(self.close)
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def confirm(self):
        print("Confirmed!")

def main():
    app = QApplication(sys.argv)
    modal = ModalDialog()
    modal.setStyleSheet("background-color: black;")  # Black background
    modal.exec_()

if __name__ == '__main__':
    main()