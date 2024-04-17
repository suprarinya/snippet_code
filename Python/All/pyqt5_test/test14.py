from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        add_button = QPushButton("Add Label", self.central_widget)
        add_button.clicked.connect(self.addLabel)
        self.layout.addWidget(add_button)

    def addLabel(self):
        print(f"Label {self.scroll_layout.count()}")

        label = QLabel(f"Label {self.scroll_layout.count()}", self.scroll_content)
        label.setObjectName(f'test{self.scroll_layout.count()}')
        self.scroll_layout.addWidget(label)

        # Scroll to the bottom by adjusting the scrollbar
        v_scrollbar = self.scroll_area.verticalScrollBar()
        v_scrollbar.setSliderPosition(v_scrollbar.maximum())
        v_scrollbar.setRange(0, v_scrollbar.maximum())
        # self.scroll_area.ensureWidgetVisible(label)  # Ensure the newly added widget is visible
        # label.setFocus()
        # lb = window.findChild(QLabel, f"test{self.scroll_layout.count()-1}") 
        # print(lb)
        # if lb:
        #     lb.setFocus()

        # v_scrollbar.setValue(v_scrollbar.maximum())


def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
