import sys
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class RealTimeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Create a QTimer to update the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

    def updateTime(self):
        # Get the current time
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss")

        # Update the label with the current time
        self.label.setText(time_text)

def main():
    app = QApplication(sys.argv)
    real_time_widget = RealTimeWidget()
    real_time_widget.setWindowTitle("Real-Time Widget")
    real_time_widget.setGeometry(100, 100, 200, 100)
    real_time_widget.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




            # self.header.resize(self.header.sizeHint())
        # self.header.resize(1400, 50)