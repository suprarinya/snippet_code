from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class BottomPart(QWidget):
    def __init__(self, hn, patientname, age, procedurename, doctorname):
        super(BottomPart, self).__init__()
        self.setStyleSheet("background-color: black;") 
        self.hglayout = QGridLayout()

        self.hnlabel = QLabel(f'Patient : {hn}', self)
        self.hnlabel.setStyleSheet("color: white; font-size: 24px;") 
        self.hnlabel.setAlignment(Qt.AlignLeft)

        self.namelabel = QLabel(f'Name (age) : {patientname} ({age})', self)
        self.namelabel.setStyleSheet("color: white; font-size: 24px;") 
        self.namelabel.setAlignment(Qt.AlignLeft)

        self.procedurelabel = QLabel(f'Procedure : {procedurename}', self)
        self.procedurelabel.setStyleSheet("color: white; font-size: 24px;") 
        self.procedurelabel.setAlignment(Qt.AlignLeft)

        self.physicianlabel = QLabel(f'Physician : {doctorname} ว.47661', self)
        self.physicianlabel.setStyleSheet("color: white; font-size: 24px;") 
        self.physicianlabel.setAlignment(Qt.AlignLeft)

        self.hglayout.addWidget(self.hnlabel, 0, 0)   
        self.hglayout.addWidget(self.namelabel, 1, 0)        
        self.hglayout.addWidget(self.procedurelabel, 0, 1)
        self.hglayout.addWidget(self.physicianlabel, 1, 1)

        self.setLayout(self.hglayout)