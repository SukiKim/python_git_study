# ch 5.4.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt # 날짜와 주요 속성값 사용을 위해 추가

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate() # 현재 날짜를 저장하기 위해 추가
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self) # 추가
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self) # 버튼추가
        self.btn2 = QPushButton('Clear', self) # 버튼 클릭시 핸들러 함수 연결

        hbox  = QHBoxLayout()
        hbox.addStretch(1) 
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()

        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1) # 수정
        vbox.addStretch(1)

        self.setLayout(vbox) # 빈공간 - 버튼

        self.setWindowTitle('Calculator')
        # self.setWindowIcon(QIcon('myself.jpg'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()


# # ch 5.2.1 ui.py
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)

# from PyQt5.QtGui import QIcon

# class View(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
#         self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

#         self.btn1 = QPushButton('Message', self) # 버튼추가
#         self.btn2 = QPushButton('Clear', self) # 버튼 클릭시 핸들러 함수 연결

#         hbox  = QHBoxLayout()
#         hbox.addStretch(1) 
#         hbox.addWidget(self.btn1)
#         hbox.addWidget(self.btn2)

#         vbox = QVBoxLayout()

#         vbox.addWidget(self.te1)
#         vbox.addLayout(hbox)
#         vbox.addStretch(1)

#         self.setLayout(vbox) # 빈공간 - 버튼

#         self.setWindowTitle('Calculator')
#         # self.setWindowIcon(QIcon('myself.jpg'))
#         self.resize(256, 256)
#         self.show()

#     def activateMessage(self):
#         self.te1.appendPlainText("Button clicked!")

#     def clearMessage(self):
#         self.te1.clear()

