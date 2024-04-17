# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Centered Window')
#         self.setGeometry(0, 0, 400, 300)

#         # Calculate the center position
#         screen = QDesktopWidget().screenGeometry()
#         self.move(int((screen.width() - self.width()) / 2), int((screen.height() - self.height()) / 2))

# def main():
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# import sys
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QProgressBar, QLabel
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# class LoadingModal(QWidget):
#     def __init__(self, parent):
#         super(LoadingModal, self).__init__(parent)
#         self.setGeometry(100, 100, 400, 200)
#         layout = QVBoxLayout(self)
        
#         self.loading_label = QLabel("Loading, please wait...")
#         self.progress_bar = QProgressBar()
#         self.progress_bar.setRange(0, 0)  # Set to indeterminate mode
        
#         layout.addWidget(self.loading_label)
#         layout.addWidget(self.progress_bar)

# class WebPageLoader(QMainWindow):
#     def __init__(self):
#         super(WebPageLoader, self).__init__()
#         self.setGeometry(100, 100, 800, 600)
        
#         self.browser = QWebEngineView()
#         self.browser.loadStarted.connect(self.showLoadingModal)
#         self.browser.loadFinished.connect(self.hideLoadingModal)
        
#         self.loading_modal = LoadingModal(self)
        
#         self.setCentralWidget(self.loading_modal)

#     def showLoadingModal(self):
#         self.loading_modal.show()
        
#     def hideLoadingModal(self):
#         self.loading_modal.hide()
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWin = WebPageLoader()
#     mainWin.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.showAlert()

    def showAlert(self):
        QMessageBox.information(self, "Alert Title", "Your alert message here.")

app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec_())