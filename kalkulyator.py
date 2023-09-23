import sys
from ifelse import *
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

class Calculyator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.txt = ''
        self.label = QLabel(self)


        self.v_boxmenu = QVBoxLayout()
        self.v_box = QVBoxLayout()
        self.v_box1 = QVBoxLayout()
        self.v_box2 = QVBoxLayout()
        self.v_box3 = QVBoxLayout()

        self.h_box = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.bush_mines = QPushButton('-')
        self.bush_plus = QPushButton('+')
        self.bush_mult = QPushButton("*")
        self.bush_division = QPushButton('/')
        self.bush_equals = QPushButton('=')
        self.bush_1 = QPushButton('(')
        self.bush_2 = QPushButton(')')
        self.bush_3 = QPushButton('🔚')

        self.bush = QPushButton('0')
        self.bush1 = QPushButton('1')
        self.bush2 = QPushButton('2')
        self.bush3 = QPushButton('3')
        self.bush4 = QPushButton('4')
        self.bush5 = QPushButton('5')
        self.bush6 = QPushButton('6')
        self.bush7 = QPushButton('7')
        self.bush8 = QPushButton('8')
        self.bush9 = QPushButton('9')

        self.h_box.addWidget(self.bush1)
        self.h_box.addWidget(self.bush2)
        self.h_box.addWidget(self.bush3)
        self.h_box.addWidget(self.bush_3)

        self.h_box1.addWidget(self.bush4)
        self.h_box1.addWidget(self.bush5)
        self.h_box1.addWidget(self.bush6)
        self.h_box1.addWidget(self.bush_mult)

        self.h_box2.addWidget(self.bush7)
        self.h_box2.addWidget(self.bush8)
        self.h_box2.addWidget(self.bush9)
        self.h_box2.addWidget(self.bush_mines)

        self.h_box3.addWidget(self.bush)
        self.h_box3.addWidget(self.bush_equals)
        self.h_box3.addWidget(self.bush_plus)

        self.h_box4.addWidget(self.bush_1)
        self.h_box4.addWidget(self.bush_2)
        self.h_box4.addWidget(self.bush_division)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)
        self.setFixedSize(600, 500)

        self.bush.clicked.connect(self.btn_bush)
        self.bush1.clicked.connect(self.btn_bush1)
        self.bush2.clicked.connect(self.btn_bush2)
        self.bush3.clicked.connect(self.btn_bush3)
        self.bush4.clicked.connect(self.btn_bush4)
        self.bush5.clicked.connect(self.btn_bush5)
        self.bush6.clicked.connect(self.btn_bush6)
        self.bush7.clicked.connect(self.btn_bush7)
        self.bush8.clicked.connect(self.btn_bush8)
        self.bush9.clicked.connect(self.btn_bush9)

        self.bush_mult.clicked.connect(self.btn_mult)
        self.bush_division.clicked.connect(self.btn_division)
        self.bush_plus.clicked.connect(self.btn_plus)
        self.bush_mines.clicked.connect(self.btn_mines)
        self.bush_equals.clicked.connect(self.btn_equals)
        self.bush_1.clicked.connect(self.btn_bush_1)
        self.bush_2.clicked.connect(self.btn_bush_2)
        self.bush_3.clicked.connect(self.btn_bush_3)


    def btn_bush(self):
        if ifsible_with_number1(self.txt):
            self.txt += '0'
            self.label.setText(self.txt)

    def btn_bush1(self):
        if ifsible_with_number(self.txt):
            self.txt += '1'
            self.label.setText(self.txt)

    def btn_bush2(self):
        if ifsible_with_number(self.txt):
            self.txt += '2'
            self.label.setText(self.txt)

    def btn_bush3(self):
        if ifsible_with_number(self.txt):
            self.txt += '3'
            self.label.setText(self.txt)

    def btn_bush4(self):
        if ifsible_with_number(self.txt):
            self.txt += '4'
            self.label.setText(self.txt)

    def btn_bush5(self):
        if ifsible_with_number(self.txt):
            self.txt += '5'
            self.label.setText(self.txt)

    def btn_bush6(self):
        if ifsible_with_number(self.txt):
            self.txt += '6'
            self.label.setText(self.txt)

    def btn_bush7(self):
        if ifsible_with_number(self.txt):
            self.txt += '7'
            self.label.setText(self.txt)

    def btn_bush8(self):
        if ifsible_with_number(self.txt):
            self.txt += '8'
            self.label.setText(self.txt)

    def btn_bush9(self):
        if ifsible_with_number(self.txt):
            self.txt += '9'
            self.label.setText(self.txt)

    def btn_mult(self):
        if ifbracket(self.txt) and ifsible(self.txt):
            self.txt += '*'
            self.label.setText(self.txt)

    def btn_division(self):
        if ifbracket(self.txt) and ifsible(self.txt):
            self.txt += '/'
            self.label.setText(self.txt)

    def btn_plus(self):
        if ifbracket(self.txt) and ifsible(self.txt):
            self.txt += '+'
            self.label.setText(self.txt)

    def btn_mines(self):
        if ifbracket(self.txt) and ifsible(self.txt):
            self.txt += '-'
            self.label.setText(self.txt)

    def btn_equals(self):
        if ifbrackets(self.txt):
            if ifbracket(self.txt) and ifsible(self.txt):
                self.label.clear()
                self.txt = str(eval(self.txt))
                self.label.setText(self.txt)

    def btn_bush_1(self):
        if ifbrakets_with_number(self.txt):
            self.txt += '('
            self.label.setText(self.txt)

    def btn_bush_2(self):
        if ifbrakets_with_number2(self.txt) and ifbrackets2(self.txt) and ifbracket(self.txt):
            self.txt += ')'
            self.label.setText(self.txt)

    def btn_bush_3(self):
            self.txt = self.txt[:-1]
            self.label.setText(self.txt)


app = QApplication(sys.argv)
win = Calculyator()
win.show()
app.exec_()


