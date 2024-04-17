# import os
# import sys

# from PIL.ImageQt import ImageQt
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtGui import QPainter
# from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
# from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton
# import tempfile

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog, QPrinter
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QApplication, QMainWindow, QAction, QFileDialog, QTextBrowser, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtPrintSupport
from pdf2image import convert_from_path


# class PrintTest(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(PrintTest, self).__init__(parent)
#         layout = QtWidgets.QHBoxLayout(self)
#         self.view = QtWebEngineWidgets.QWebEngineView()

#         settings = self.view.settings()
#         settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

#         url = QtCore.QUrl.fromLocalFile("D:\\laragon\\htdocs\\store\\TEST20231017\\2023-10-17\\pdf\\65434a6e00a25340870bf7bd.pdf")

#         layout.addWidget(self.view)

#         self.view.load(url)

#         self.view.page().printRequested.connect(self.printRequested)

#         # self.page = QtWebEngineWidgets.QWebEnginePage(self)
#         # self.view.setPage(self.page)
#         # self.view.printRequested.connect(self.printRequested)
#         # self.view.printRequested.connect(self.printRequested)

#         # load a page that has a print request
#         # self.view.load(QtCore.QUrl(
#         #     "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_print"))
#         # self.view.load(QtCore.QUrl(
#         #     "http://localhost/store/TEST20231017/2023-10-17/pdf/65434a6e00a25340870bf7bd.pdf"))

        
        

#     def printRequested(self):
#         defaultPrinter = QtPrintSupport.QPrinter(
#             QtPrintSupport.QPrinterInfo.defaultPrinter())
#         dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
#         if dialog.exec():
#             # printer object has to be persistent
#             self._printer = dialog.printer()
#             self.page.print(self._printer, self.printResult)

#     def printResult(self, success):
#         if success:
#             QtWidgets.QMessageBox.information(self, 'Print completed', 
#                 'Printing has been completed!', QtWidgets.QMessageBox.Ok)
#         else:
#             QtWidgets.QMessageBox.warning(self, 'Print failed', 
#                 'Printing has failed!', QtWebEngineWidgets.QMessageBox.Ok)
#             self.printRequested()
#         del self._printer


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = PrintTest()
#     mainWin.show()
#     sys.exit(app.exec_())


class PrintTest(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PrintTest, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout(self)
        self.view = QtWebEngineWidgets.QWebEngineView()
        layout.addWidget(self.view)
        self.page = QtWebEngineWidgets.QWebEnginePage(self)
        self.view.setPage(self.page)
        self.page.printRequested.connect(self.printRequested)
        # load a page that has a print request
        self.view.load(QtCore.QUrl(
            "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_print"))

    def printRequested(self):
        defaultPrinter = QtPrintSupport.QPrinter(
            QtPrintSupport.QPrinterInfo.defaultPrinter())
        dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
        if dialog.exec():
            # printer object has to be persistent
            self._printer = dialog.printer()
            self.page.print(self._printer, self.printResult)

    def printResult(self, success):
        if success:
            QtWidgets.QMessageBox.information(self, 'Print completed', 
                'Printing has been completed!', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, 'Print failed', 
                'Printing has failed!', QtWebEngineWidgets.QMessageBox.Ok)
            self.printRequested()
        del self._printer

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = PrintTest()
    mainWin.show()
    sys.exit(app.exec_())