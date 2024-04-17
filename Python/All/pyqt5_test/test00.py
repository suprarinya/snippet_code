from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QApplication

class MyObject(QObject):
    @pyqtSlot()
    def my_slot(self):
        print("Slot called")

if __name__ == "__main__":
    app = QApplication([])
    view = QWebEngineView()
    channel = QWebChannel()
    my_object = MyObject()
    channel.registerObject("myObject", my_object)
    view.page().setWebChannel(channel)
    view.setHtml('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>PyQt5 WebChannel Example</title>
        </head>
        <body>
            <button onclick="pyqt.my_slot()">Call Slot</button>
            <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
            <script>
                new QWebChannel(qt.webChannelTransport, function(channel) {
                    window.pyqt = channel.objects.myObject;
                });
            </script>
        </body>
        </html>
    ''')
    view.show()
    app.exec_()