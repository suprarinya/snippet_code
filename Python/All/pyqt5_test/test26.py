from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QLabel
import sys

def load_font(font_path, font_size=12):
    """
    Load a custom font from a file and return a QFont object.

    :param font_path: Path to the font file.
    :param font_size: Desired font size.
    :return: QFont object or None if font loading fails.
    """
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print("Failed to load font.")
        return None

    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    return QFont(font_family, font_size)

# Example usage
app = QApplication(sys.argv)

font = load_font("font/THSarabunNew Bold.ttf", 12)
if font:
    label = QLabel("Hello, custom font!")
    label.setFont(font)
    label.show()

sys.exit(app.exec_())
