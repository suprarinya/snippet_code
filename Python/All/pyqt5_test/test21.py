import sys, requests
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QFrame, QLabel, QTextEdit
from PyQt5.QtGui import QPainter, QPixmap, QImage
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtCore import Qt

class PrintDialog(QDialog):
    def __init__(self, image_url):
        super().__init__()

        self.setWindowTitle("Custom Print Dialog with Preview")
        self.setGeometry(100, 100, 600, 400)

        self.image_url = image_url

        layout = QVBoxLayout()

        image = QImage()
        image.loadFromData(requests.get(image_url).content)

        # Load the image from the URL and display it in a QLabel
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap(image))
        # pixmap = self.load_image_from_url(self.image_url)
        # print(pixmap)
        # self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)

        # Add a Print button
        self.print_button = QPushButton("Print")
        self.print_button.clicked.connect(self.print_image)
        layout.addWidget(self.print_button)

        # Add a preview frame
        self.preview_frame = QFrame()
        self.preview_frame.setFrameShape(QFrame.StyledPanel)
        self.preview_layout = QVBoxLayout()

        # Create a QLabel for a preview (placeholder)
        self.preview_label = QLabel("Preview Image")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_layout.addWidget(self.preview_label)

        self.preview_frame.setLayout(self.preview_layout)
        layout.addWidget(self.preview_frame)

        self.setLayout(layout)

    def load_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image = QImage()
            if image.loadFromData(image_data):
                pixmap = QPixmap.fromImage(image)
                return pixmap

        # If the image cannot be loaded, return an empty pixmap
        return QPixmap()

    def print_image(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            # Set the preview label text (placeholder)
            self.preview_label.setText("Printing the image...")

            # Create a painter and print the image
            painter = QPainter()
            painter.begin(printer)
            pixmap = self.load_image_from_url(self.image_url)
            if not pixmap.isNull():
                painter.drawPixmap(10, 10, pixmap)
            painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # url_image = 'https://live.staticflickr.com/65535/49251422908_591245c64a_c_d.jpg'

    # Replace 'your_image_url_here' with the actual URL of your localhost image
    dialog = PrintDialog("http://localhost/endoindex/recorder/print/65434a6e00a25340870bf7bd")
    # dialog = PrintDialog(url_image)

    dialog.exec_()

    sys.exit(app.exec_())