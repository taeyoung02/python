from PyQt5 import QtWidgets
from PyQt5 import QtCore
import datetime,time
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def time_chker(func):
    def inner_function(*args, **kwargs):
        start_time=time.time()
        result=func(*args,**kwargs) #test1() 실행값
        end_time=time.time()
        print("func:{}, time:{}".format(func.__name__,end_time-start_time))
        return result
    return inner_function #result리턴

class MyClock(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        # 스톱와치 용 변수
        self.watch_start_time = 0
        self.mouseClick = False
        self.setWindowTitle("시계")
        self.initWidgets()
        self.setFixedSize(250, 100)#사이즈고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)#타이틀바 없앰
        self.show()
        self.days = datetime.date.today().day
        self.months=datetime.date.today().month

    def keyPressEvent(self, e):#esc누르면 종료
        if e.key() == QtCore.Qt.Key_Escape:
            day = str(self.months)+"/"+str(self.days)
            try:
                print('1')
                data = pd.read_csv('C:\\python\\graph.csv')
                print('2')
                
                if data["day"].isin([day]):
                    print('3')
                    data.loc[data["day"]==day, "time"]+=self.watch_start_time
                    print("ok")
                else:
                    print('4')
                    data.loc[data["day"]==day, "time"]+=self.watch_start_time
                    data.append([day,self.watch_start_time])
                    print('o')
            except:
                df=pd.DataFrame([[day,self.watch_start_time]],\
                    columns=['day', 'time'])
                print('k')
                df.to_csv('graph.csv',header=True, index=False)#header:column이름 정보
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
        self.layout = QtWidgets.QVBoxLayout(self) #QV=가로 QH=세로

        # 시작, 초기화 버튼 2개를 HBoxLayout 에 추가합니다.
        self.button_layout = QtWidgets.QHBoxLayout(self) # 버튼을 담기위한 레이아웃
        self.btn_start = QtWidgets.QPushButton("중지", self)
        self.btn_reset = QtWidgets.QPushButton("초기화", self)
        self.btn_start.resize(self.btn_start.sizeHint())
        self.btn_reset.resize(self.btn_start.sizeHint())
        self.button_layout.addWidget(self.btn_start)
        self.button_layout.addWidget(self.btn_reset)

        self.lcd = QtWidgets.QLCDNumber()#시계디자인 위젯
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)#글자평평하게
        self.lcd.setDigitCount(8)#글자 총 8개까지 보여줌(hh:mm:ss)
        self.lcd.setFrameStyle(QtWidgets.QFrame.NoFrame)#박스없앰

        self.timer = QtCore.QTimer()    # 타이머 생성
        # self.timer.timeout.connect(self.show_time)    # 타임아웃 이벤트를 show_time과 연결
        # 스탑와치용 출력 함수 연결
        self.timer.timeout.connect(self.showWatch)  # 타임아웃 이벤트를 show_time과 연결
        # 정한 시간이 지날때마다 show_time 실행
        self.timer.start(1000)#1초에 한번씩

        self.resetWatch()
        self.layout.addWidget(self.lcd)
        # 버튼 레이아웃을 기본 레이아웃에 추가합니다.
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

        self.btn_start.clicked.connect(self.startWatch)
        self.btn_reset.clicked.connect(self.resetWatch)
    
    def startWatch(self):
        '''스탑와치를 시작하는 함수 입니다.
        버튼 클릭시 시작과 중지를 한 버튼으로 처리하기 위해
        버튼의 글자를 가져와서 각 상황에 맞게 동작합니다.'''
        text = self.btn_start.text()
        if text == "시작":
            self.btn_start.setText("중지")
            self.timer.start(1000)
        elif text == "중지":
            self.btn_start.setText("시작")
            self.timer.stop()
     
    def resetWatch(self):
        '''스탑와치를 초기화 합니다.'''
        text = "00:00:00"
        self.watch_start_time = 0
        self.lcd.display(text)
    
    def showWatch(self):
        '''스탑와치의 현재시간 - 시작시간을 계산해서 화면에 출력하는 함수'''
        # 현재시간 - 스탑와치 시작시간을 total_seconds() 로 변환해서 초만 받습니다.
        self.watch_start_time+=1
        # 진행된 초를 시:분:초로 출력하기 위해서 계산합니다.
        hour = self.watch_start_time // 3600
        minute = self.watch_start_time % 3600 // 60
        second = self.watch_start_time % 60
        # 시:분:초 형태로 문자열 포맷팅을 합니다.
        text = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
        # 출력
        self.lcd.display(text)


app = QtWidgets.QApplication([])
win = MyClock()
app.exec_()