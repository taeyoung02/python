from PyQt5 import QtWidgets
from PyQt5 import QtCore

class MyClock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.mouseClick = False

        self.setWindowTitle("시계")
        self.initWidgets()
        self.setFixedSize(250, 100)#사이즈고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)#타이틀바 없앰
        self.show()
    
    def keyPressEvent(self, e):#esc누르면 종료
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):#마우스로 창 누를때
        if e.button() == QtCore.Qt.LeftButton:#좌클릭시
            self.mouseClick = True
            self.oldPos = e.globalPos()#x,y가 튜플형태로 넘어옴
            #globalPos=윈도우상의 x,y좌표
    def mouseReleaseEvent(self, e):
        self.mouseClick = False

    def mouseMoveEvent(self, e):#마우스로 창 누른뒤 이동시킬때
        if self.mouseClick:
            delta = QtCore.QPoint(e.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = e.globalPos()


    def initWidgets(self):
        self.layout = QtWidgets.QVBoxLayout()#QV=가로 QH=세로
        self.lcd = QtWidgets.QLCDNumber()#시계디자인 위젯
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)#글자평평하게
        self.lcd.setDigitCount(8)#글자 총 8개까지 보여줌(hh:mm:ss)
        self.lcd.setFrameStyle(QtWidgets.QFrame.NoFrame)#박스없앰

        self.timer = QtCore.QTimer()#타이머 생성
        self.timer.timeout.connect(self.show_time)#타임아웃 이벤트를 show_time과 연결
        #정한 시간이 지날때마다 show_time 실행
        
        self.timer.start(1000)#1초에 한번씩

        self.show_time()

        self.layout.addWidget(self.lcd)
        self.setLayout(self.layout)
    
    def show_time(self):
        time = QtCore.QTime.currentTime()#현재시간
        self.currentTime = time.toString("hh:mm:ss")#모양을 만듬
        self.lcd.display(self.currentTime)

app = QtWidgets.QApplication([])
win = MyClock()
app.exec_()