import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Create the scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                width: 0px;
            }
            QScrollBar:horizontal {
                height: 0px;
            }
        """)

        # Create a container widget and layout
        container = QWidget()
        container_layout = QVBoxLayout()

        # Add some sample widgets
        for i in range(30):
            label = QLabel(f"Label {i+1}", self)
            container_layout.addWidget(label)

        container.setLayout(container_layout)
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
