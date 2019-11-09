#thread 멀티태스킹으로 동시에 여러 프로세스를 사용

import threading #쓰레딩 클래스 가져옴
class Messenger(threading.Thread): 
    def run(self):
        for _ in range(10):#변수상관없이 루프만 돌고싶을때 _ 사용
            print(threading.currentThread().getName())


x = Messenger(name="메세지를 보냅니다\n")
y = Messenger(name="메세지를 수신합니다")

x.start()

y.start()

#원래 x가 모두 출력하고 y를 출력하는데 멀티태스킹으로 동시실행하여
#x,y번갈아 실행됌

