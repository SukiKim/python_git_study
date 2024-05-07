# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit
# QMessageBox: 메세지박스 위젯
from PyQt5.QtGui import QIcon # Icon 추가를 위한 라이브러리

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self) # 버튼추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        vbox  = QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        vbox.addStretch(1) # 빈공간
        vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addStretch(1) # 빈공간

        self.setLayout(vbox) # 빈공간 - 버튼


        self.setWindowTitle('Calculator312312')
        # self.setWindowIcon(QIcon('myself.jpg'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수: 메세지 박스 출력
        QMessageBox.information(self,"information", "button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())