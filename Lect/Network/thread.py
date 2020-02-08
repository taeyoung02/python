import time
import threading

def 주문받기():
    for i in range(5):
        print("주문받기 {}".format(i))
        time.sleep(1)

def 우편발송():
    for i in range(5):
        print("우편발송 {}".format(i))
        time.sleep(1)
#프로세스=공장, 쓰레드=일꾼
th1 = threading.Thread(target=주문받기)
th2 = threading.Thread(target=우편발송)

th1.daemon=True#메인이끝나면 쓰레드도 중간에 끝남
th2.daemon=True
#프로그램 전체는 메인쓰레드
#메인쓰레드가 쓰레드들을 관장
th1.start()
th2.start()