from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1=QPushButton('Message',self)
        self.btn2=QPushButton('Clear',self)
        
        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        
        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/'])
        
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
        
    def activateMessage(self, text):
        self.te1.appendPlainText(text)
        
    def clearMessage(self):
        self.te1.clear()

# from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
#                              QMessageBox, QPlainTextEdit, QHBoxLayout,
#                              QLineEdit, QComboBox)
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtCore


# class View(QWidget):
    
#     def __init__(self):
#         super().__init__()
#         self.initUI()
        
#     def initUI(self):
#         self.te1 = QPlainTextEdit()
#         self.te1.setReadOnly(True)
        
#         self.btn1=QPushButton('Calc',self)
#         self.btn2=QPushButton('Clear',self)
        
#         self.le1=QLineEdit('0',self)
#         self.le1.setAlignment(QtCore.Qt.AlignRight)
#         self.le1.setFocus(True)
#         self.le1.selectAll()
        
#         self.le2=QLineEdit('0',self)
#         self.le2.setAlignment(QtCore.Qt.AlignRight)
        
#         self.cb = QComboBox(self)
#         self.cb.addItems(['+', '-', '*', '/'])
        
#         hbox_formular = QHBoxLayout()
#         hbox_formular.addWidget(self.le1)
#         hbox_formular.addWidget(self.cb)
#         hbox_formular.addWidget(self.le2)
        
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(self.btn1)
#         hbox.addWidget(self.btn2)
        
#         vbox=QVBoxLayout()
#         vbox.addWidget(self.te1)
#         vbox.addLayout(hbox_formular)
#         vbox.addLayout(hbox)
#         vbox.addStretch(1)
        
#         self.setLayout(vbox)
        
#         self.setWindowTitle('Calculator')
#         self.setWindowIcon(QIcon('icon.png'))
#         self.resize(256,256)
#         self.show()
        
#     def setDisplay(self):
#         self.te1.appendPlainText("Button clicked!")
        
#     def clearMessage(self):
#         self.te1.clear()

# # ch 5.2.1 ui.py
# #from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)

# #from PyQt5.QtGui import QIcon

# #class View(QWidget):

# #    def __init__(self):
# #        super().__init__()
# #        self.initUI()

# #    def initUI(self):
# #        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
# #        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

# #        self.btn1 = QPushButton('Message', self) # 버튼추가
# #        self.btn2 = QPushButton('Clear', self) # 버튼 클릭시 핸들러 함수 연결

# #        hbox  = QHBoxLayout()
# #        hbox.addStretch(1) 
# #        hbox.addWidget(self.btn1)
# #        hbox.addWidget(self.btn2)

# #        vbox = QVBoxLayout()

# #       vbox.addWidget(self.te1)
# #        vbox.addLayout(hbox)
# #        vbox.addStretch(1)
# #
# #        self.setLayout(vbox) # 빈공간 - 버튼

# #        self.setWindowTitle('Calculator')
# #        # self.setWindowIcon(QIcon('myself.jpg'))
# #        self.resize(256, 256)
# #        self.show()

# #    def activateMessage(self):
# #        self.te1.appendPlainText("Button clicked!")

# #    def clearMessage(self):
# #        self.te1.clear()
