#thread 멀티태스킹으로 동시에 여러 프로세스를 사용

import threading
class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):#변수상관없이 루프만 돌고싶을때 _ 사용
            print(threading.currentThread().getName())


x = Messenger(name="메세지를 보냅니다\n")
y = Messenger(name="메세지를 수신합니다")

x.start()

y.start()

