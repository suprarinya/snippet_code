# from PyQt5.QtWidgets import *


# class MyList(QScrollArea):
#     def __init__(self):
#         super().__init__()
#         self._widget = QWidget()
#         self._layout = QVBoxLayout()
        
#         # If I comment this line, MyButton._add function will not work, and the screen will not display new widget.
#         self._layout.addWidget(QPushButton('test'))

#         # set layout and widget
#         self._widget.setLayout(self._layout)
#         self.setWidget(self._widget)

#         # display settings
#         self.setWidgetResizable(True)


# class MyButton(QPushButton):
#     def __init__(self, text, _list):
#         super().__init__(text=text)
#         self._list = _list
#         self.clicked.connect(self._add)
    

#     def _add(self):
#         self._list._layout.addWidget(QPushButton('test'))


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self._layout = QVBoxLayout()
#         self._my_list = MyList()
#         self._my_button = MyButton(text='Add', _list=self._my_list)
#         self._layout.addWidget(self._my_list)
#         self._layout.addWidget(self._my_button)

#         # set layout
#         self.setLayout(self._layout)

#         # display settings
#         self.setWindowTitle('My Demo')


# def main():
#     app = QApplication([])
#     main_window = MainWindow()

#     main_window.show()
#     app.exec_()


# if __name__ == "__main__":
#     main()   

import json

data = '{"patientname":"test  test","doctorname":"\u0e19\u0e1e.\u0e01\u0e23\u0e34\u0e0a \u0e2d\u0e31\u0e2a\u0e2a\u0e31\u0e19\u0e15\u0e0a\u0e31\u0e22","procedurename":"Liver Biopsy","age":20,"hn":"TEST20231106","appointment":"2023-11-06","cid":"6548b622e689b8977e03e1de","open":"capture","event":"case_data","python":true}'

if data is not None and data != '':
    if '{' in data and '"event"' in data:
        try:
            # Attempt to parse the JSON data
            parse = json.loads(data)

            # Process or print the parsed JSON data as needed
            print(json.dumps(parse, ensure_ascii=False))

            print(parse['event'])

        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print(f"JSON parsing error: {e}")

    else:
        print("Data doesn't contain JSON content")

else:
    print("Data is None or empty")

from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)