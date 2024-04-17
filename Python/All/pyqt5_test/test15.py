import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtCore import Qt  # Import the Qt module

class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.progress_bar = QProgressBar(self.central_widget)
        self.layout.addWidget(self.progress_bar)

        # Center the progress bar
        self.progress_bar.setAlignment(Qt.AlignCenter)  # Use Qt.AlignCenter from the Qt module

        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.updateProgress)

        self.show()

    def updateProgress(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)
        else:
            self.progress_timer.stop()
            self.close()

    def startLoading(self):
        self.progress_bar.setValue(0)
        self.progress_timer.start(50)  # Adjust the timer interval as needed

def main():
    app = QApplication(sys.argv)
    loading_window = LoadingWindow()
    loading_window.startLoading()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
