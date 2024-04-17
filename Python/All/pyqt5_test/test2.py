# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl
# from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog, QPrinter
# from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QApplication, QMainWindow, QAction, QFileDialog, QTextBrowser, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem


import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


def main():

    print(
        f"PyQt5 version: {QtCore.PYQT_VERSION_STR}, Qt version: {QtCore.QT_VERSION_STR}"
    )

    app = QtWidgets.QApplication(sys.argv)
    # filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, filter="PDF (*.pdf)")
    # if not filename:
    #     print("please select the .pdf file")
    #     sys.exit(0)
    view = QtWebEngineWidgets.QWebEngineView()
    settings = view.settings()
    settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
    url = QtCore.QUrl.fromLocalFile("D:\\laragon\\htdocs\\store\\TEST20231017\\2023-10-17\\pdf\\65434a6e00a25340870bf7bd.pdf")
    view.load(url)
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
