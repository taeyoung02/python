from selenium import webdriver
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QToolButton, QSizePolicy, QLabel, QLineEdit,QPushButton
import random
import keyboard
import re
# options=webdriver.ChromeOptions()
# options.add_argument('headless')#창을 안띄우는 headless모드
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")#gpu가속 끔
# #user-agent값을 변경하여 headless모드 감지를 방지
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR") #headless모드에선 언어설정이 안되있으므로 한국어로 설정(감지 방지)
driver = webdriver.Chrome('C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe')#,chrome_options=options)
class start(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QtWidgets.QHBoxLayout(self)

        self.id_layout = QtWidgets.QVBoxLayout(self)
        self.pwd_layout = QtWidgets.QVBoxLayout(self) #QV=가로 QH=세로

        self.id=QLabel("ID")
        self._id=QLineEdit()
        self.pwd=QLabel("password")
        self._pwd=QLineEdit()

        self.id_layout.addWidget(self.id)
        self.id_layout.addWidget(self._id)

        self.pwd_layout.addWidget(self.pwd)
        self.pwd_layout.addWidget(self._pwd)
        self.layout.addLayout(self.id_layout)
        self.layout.addLayout(self.pwd_layout)

        self.setLayout(self.layout)

        self._pwd.setEchoMode(QLineEdit.Password)
        self._pwd.returnPressed.connect(self.login)

        self.show()

    def login(self):
        driver.get("https://www.instagram.com/accounts/login/")
        driver.implicitly_wait(10)

        driver.find_element_by_name('username').send_keys(self._id.text())
        driver.find_element_by_name('password').send_keys(self._pwd.text())
        driver.implicitly_wait(10)
        driver.find_elements_by_tag_name('button')[1].click()
        driver.implicitly_wait(100)
        self.newWindow = Main()
        self.newWindow.show()
        self.close()
        
class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout_m = QtWidgets.QHBoxLayout(self) #전체틀
        self.start_layout = QtWidgets.QVBoxLayout() #버튼을 담을 틀
        self.setFixedSize(300, 200)
        self.target=QLabel("상대의 아이디를 입력하세요")
        self._target=QLineEdit()
        self.like = self.createButton("좋아요",self.clicklike)#버튼watch
        #self.comment = self.createButton("댓글",self.clickcomment)#버튼graph
    
        self.like.resize(self.like.sizeHint())#sizeHint=holds the recommended size for the widget
        #self.comment.resize(self.comment.sizeHint())

        #틀에 버튼 담음
        #self.start_layout.addWidget(self.comment)
        self.start_layout.addWidget(self.target)
        self.start_layout.addWidget(self._target)
        self.layout_m.addLayout(self.start_layout)#전체틀에 버튼을 담은 틀을 담음
        self.layout_m.addWidget(self.like)
        self.setLayout(self.layout_m)
       
        self.show()
        
        self.timer = QtCore.QTimer()    # 타이머 생성
        
        # 함수 연결
        self.timer.timeout.connect(self.clicklike)  # 타임아웃 이벤트를 showWatch와 연결
        # 정한 시간이 지날때마다 show_time 실행
        self.timer.start(1000*60*60)#1시간에 한번씩


    def clicklike(self):
        # driver.find_element_by_name('username').send_keys("01037395297")
        # driver.find_element_by_name('password').send_keys("dh241152!")
        driver.get('https://www.instagram.com/{}'.format(self._target.text()))
        # driver.get('https://www.instagram.com/{}/'.format(input_target_id))
        #첫번째 게시글 클릭
        driver.find_elements_by_css_selector('.v1Nh3.kIKUG._bz0w')[0].find_element_by_tag_name('a').click()
        driver.implicitly_wait(10)
        #좋아요누르기
        driver.get(driver.current_url)
        temp1=driver.find_elements_by_class_name('eo2As ')
        temp1[0].find_element_by_class_name('wpO6b ').click()
        #사진의 정보가져와서 필요한데이터 추출
        img_information=driver.find_elements_by_tag_name('img')[1].get_attribute('alt')
        img_information=img_information.split(': ')
        img_information=img_information[1].split(' and ')
        #print(img_information)
        food = ["맛있겠네","맛있어 보이는구나!","다음에 나도 데려가~~", "돼지야!"]
        people=["오 아주 잘나왔군!", "정말 멋쟁이군", "우도환 닮았다", "손나은 닮았다"]

        for i in img_information:
            if re.search('people',i):
                case="인물"
                break
            if re.search('food',i):
                case="음식"
                break
            else:
                case="기타"

        if case=="인물":
            rand_number=random.randint(0,3)
            comment=people[rand_number]
        elif case=="음식":
            rand_number=random.randint(0,3)
            comment=food[rand_number]
        else:
            comment="^^7"
        #댓글입력
        temp1[0].find_elements_by_class_name('wpO6b ')[1].click()
        driver.find_element_by_tag_name('textarea').send_keys(comment)
        driver.implicitly_wait(10)
        driver.find_element_by_class_name('X7cDz').find_element_by_tag_name('button').click()
    
    
    def createButton(self, text, function):
        button = Button(text)
        button.clicked.connect(function)
        return button



class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        buttonStyle = '''
        QToolButton:hover {border:1px solid #0078d7; background-color:#e5f1fb;}
        QToolButton:pressed {background-color:#a7c8e3}
        QToolButton {font-size:11pt; font-family:나눔고딕; border:1px solid #d6d7d8; background-color:#f0f1f1}
        '''
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.setStyleSheet(buttonStyle)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win=start()
    app.exec_()