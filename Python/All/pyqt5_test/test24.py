import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtPrintSupport

# class PrintTest(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(PrintTest, self).__init__(parent)
#         layout = QtWidgets.QVBoxLayout(self)

#         # Create a button for printing
#         self.print_button = QtWidgets.QPushButton("Print")
#         layout.addWidget(self.print_button)

#         self.view = QtWebEngineWidgets.QWebEngineView()
#         layout.addWidget(self.view)

#         self.page = QtWebEngineWidgets.QWebEnginePage(self)
#         self.view.setPage(self.page)
#         self.page.printRequested.connect(self.printRequested)

#         # load a page that you want to print
#         self.view.load(QtCore.QUrl("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_print"))

#         # Connect the button to the printRequested function
#         self.print_button.clicked.connect(self.printRequested)

#     def printRequested(self):
#         defaultPrinter = QtPrintSupport.QPrinter(QtPrintSupport.QPrinterInfo.defaultPrinter())
#         dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
#         if dialog.exec():
#             self._printer = dialog.printer()
#             self.page.print(self._printer, self.printResult)

#     def printResult(self, success):
#         if success:
#             QtWidgets.QMessageBox.information(self, 'Print completed', 
#                 'Printing has been completed!', QtWidgets.QMessageBox.Ok)
#         else:
#             QtWidgets.QMessageBox.warning(self, 'Print failed', 
#                 'Printing has failed!', QtWidgets.QMessageBox.Ok)
#         del self._printer

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = PrintTest()
#     mainWin.show()
#     sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtPrintSupport

class PrintTest(QtWidgets.QWidget):
    def __init__(self, pdf_file, parent=None):
        super(PrintTest, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        # Create a button for printing
        self.print_button = QtWidgets.QPushButton("Print")
        layout.addWidget(self.print_button)

        self.view = QtWebEngineWidgets.QWebEngineView()
        layout.addWidget(self.view)

        self.page = QtWebEngineWidgets.QWebEnginePage(self)
        self.view.setPage(self.page)
        settings = self.view.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.page.printRequested.connect(self.printRequested)

        # Set the URL to the local PDF file using a file:/// URL
        file_url = QtCore.QUrl.fromLocalFile(pdf_file)
        self.view.setUrl(file_url)

        # Connect the button to the printRequested function
        self.print_button.clicked.connect(self.printRequested)

    def printRequested(self):
        defaultPrinter = QtPrintSupport.QPrinter(QtPrintSupport.QPrinterInfo.defaultPrinter())
        dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
        if dialog.exec():
            self._printer = dialog.printer()
            self.page.print(self._printer, self.printResult)

    def printResult(self, success):
        if success:
            QtWidgets.QMessageBox.information(self, 'Print completed', 
                'Printing has been completed!', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, 'Print failed', 
                'Printing has failed!', QtWidgets.QMessageBox.Ok)
        del self._printer

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pdf_file = "D:\\laragon\\htdocs\\store\\TEST20231017\\2023-10-17\\pdf\\65434a6e00a25340870bf7bd.pdf"
    mainWin = PrintTest(pdf_file)
    mainWin.show()
    sys.exit(app.exec_())