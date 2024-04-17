import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QScrollArea
from PyQt5.QtCore import pyqtSignal, QObject

class FirstWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.scroll_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        self.scroll_layout = QVBoxLayout(self.scroll_widget)

    def add_label(self, text):
        label = QLabel(text)
        self.scroll_layout.addWidget(label)

class SecondWidget(QWidget):
    update_signal = pyqtSignal(str)

    def __init__(self, first_widget):
        super().__init__()
        self.first_widget = first_widget
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.addButton = QPushButton('Add Label')
        self.addButton.clicked.connect(self.add_label)
        self.layout.addWidget(self.addButton)

    def add_label(self):
        text = 'New Label'
        self.first_widget.add_label(text)
        self.update_signal.emit(text)

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    first_widget = FirstWidget()
    second_widget = SecondWidget(first_widget)
    second_widget.update_signal.connect(first_widget.add_label)

    layout.addWidget(first_widget)
    layout.addWidget(second_widget)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
