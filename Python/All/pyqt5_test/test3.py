import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QScrollArea

class DynamicWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dynamic Widget Example')
        self.setGeometry(100, 100, 400, 300)

        # Create a QScrollArea to contain the content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a container widget for the QVBoxLayout
        scroll_container = QWidget()
        scroll_area.setWidget(scroll_container)

        self.layout = QVBoxLayout(scroll_container)

        self.addButton = QPushButton('Add Label')
        self.addButton.clicked.connect(self.add_label)
        self.layout.addWidget(self.addButton)

        # Add the QScrollArea to this QWidget
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)

    def add_label(self):
        label = QLabel('New Label')
        self.layout.addWidget(label)

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    main_widget = DynamicWidgetExample()
    window.setCentralWidget(main_widget)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
