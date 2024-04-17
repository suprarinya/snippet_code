# import os
# import sys

# from PIL.ImageQt import ImageQt
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtGui import QPainter
# from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
# from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton
# import tempfile

# from pdf2image import convert_from_path


# class PrintDemo(QMainWindow):

#     def __init__(self):
#         QMainWindow.__init__(self)

#         self.setMinimumSize(QSize(192, 128))
#         self.setWindowTitle("Print Demo")

#         printButton = QPushButton('Print', self)
#         printButton.clicked.connect(self.onPrint)
#         printButton.resize(128, 32)
#         printButton.move(32, 48)

#     def onPrint(self):
#         self.printDialog()

#     def printDialog(self):
#         filePath, filter = QFileDialog.getOpenFileName(self, 'Open file', '', 'PDF (*.pdf)')
#         if not filePath:
#             return
#         file_extension = os.path.splitext(filePath)[1]

#         if file_extension == ".pdf":
#             printer = QPrinter(QPrinter.HighResolution)
#             dialog = QPrintDialog(printer, self)
#             if dialog.exec_() == QPrintDialog.Accepted:
#                 with tempfile.TemporaryDirectory() as path:
#                     images = convert_from_path(filePath, dpi=300, output_folder=path)
#                     painter = QPainter()
#                     painter.begin(printer)
#                     for i, image in enumerate(images):
#                         if i > 0:
#                             printer.newPage()
#                         rect = painter.viewport()
#                         qtImage = ImageQt(image)
#                         qtImageScaled = qtImage.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
#                         painter.drawImage(rect, qtImageScaled)
#                     painter.end()
#         else:
#             pass


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = PrintDemo()
#     mainWin.show()
#     sys.exit(app.exec_())

# from PyQt5 import QtWidgets, QtPrintSupport, QtWebEngineWidgets, QtCore
# from PyQt5.QtPrintSupport import QPrintPreviewDialog

# class PrintWidget(QtWidgets.QWidget):
#     def __init__(self, pdf_file):
#         super(PrintWidget, self).__init__()
#         layout = QtWidgets.QVBoxLayout(self)

#         self.view = QtWebEngineWidgets.QWebEngineView()
#         self.page = QtWebEngineWidgets.QWebEnginePage(self)
#         self.view.setPage(self.page)
#         layout.addWidget(self.view)

#         pdf_file = 'D://laragon/htdocs/store/test04/2023-12-12/pdf/65783e4388af1a81500befdf.pdf'

#         # self.page = QtWebEngineWidgets.QWebEnginePage(self)
#         # self.view.setPage(self.page)
#         settings = self.view.settings()
#         settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

#         file_url = QtCore.QUrl.fromLocalFile(pdf_file)
#         self.view.setUrl(file_url)

#         self.print_button = QtWidgets.QPushButton("Print Preview", self)
#         layout.addWidget(self.print_button)
#         self.print_button.clicked.connect(self.showPrintPreview)

#     def showPrintPreview(self):
#         dialog = QPrintPreviewDialog()
#         dialog.paintRequested.connect(self.printPreview)
#         dialog.exec_()

#     def printPreview(self, printer):
#         self.page.print(printer, lambda ok: None)

# # Example Usage
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = PrintWidget('path/to/your/file.pdf')
#     mainWin.show()
#     sys.exit(app.exec_())

# from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtPrintSupport

# class PrintWidget(QtWidgets.QWidget):
#     def __init__(self, pdf_file):
#         super(PrintWidget, self).__init__()
#         layout = QtWidgets.QVBoxLayout(self)

#         self.view = QtWebEngineWidgets.QWebEngineView()
#         layout.addWidget(self.view)

#         self.page = QtWebEngineWidgets.QWebEnginePage(self)
#         self.view.setPage(self.page)
#         self.page.loadFinished.connect(self.onLoadFinished)

#         settings = self.view.settings()
#         settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

#         self.print_button = QtWidgets.QPushButton("Print Preview")
#         layout.addWidget(self.print_button)
#         self.print_button.clicked.connect(self.showPrintPreview)

#         pdf_file = 'D://laragon/htdocs/store/test04/2023-12-12/pdf/65783e4388af1a81500befdf.pdf'
#         file_url = QtCore.QUrl.fromLocalFile(pdf_file)
#         self.view.setUrl(file_url)

#     def onLoadFinished(self, ok):
#         if ok:
#             self.print_button.setEnabled(True)

#     def showPrintPreview(self):
#         dialog = QtPrintSupport.QPrintPreviewDialog()
#         dialog.paintRequested.connect(self.page.print)
#         dialog.exec_()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     pdf_file = 'path/to/your/file.pdf'  # Replace with your PDF file path
#     printWidget = PrintWidget(pdf_file)
#     printWidget.show()
#     sys.exit(app.exec_())


from PyQt5 import QtChart, QtCore, QtGui, QtPrintSupport, QtWidgets 
import sys
import random

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Chart Printing'))
        self.chart = QtChart.QChart()
        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handle_preview)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handle_print)               
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.chart_view, 0, 0, 1, 2)
        layout.addWidget(self.buttonPreview, 1, 0)        
        layout.addWidget(self.buttonPrint, 1, 1)
        self.create_chart()

    def create_chart(self):
        self.chart.setTitle("Chart Print Preview and Print Example") 
        for i in range(5):     
            series = QtChart.QLineSeries()     
            series.setName("Line {}".format(i + 1))
            series.append(0, 0)
            for i in range(1, 10):
                series.append(i, random.randint(1, 9))
            series.append(10, 10)
            self.chart.addSeries(series)
        self.chart.createDefaultAxes() 

    def handle_print(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handle_paint_request(printer)

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec_()

    def handle_paint_request(self, printer):
        painter = QtGui.QPainter(printer)
        painter.setViewport(self.chart_view.rect())
        painter.setWindow(self.chart_view.rect())                        
        self.chart_view.render(painter)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())