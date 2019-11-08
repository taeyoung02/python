#모든 예외는 Exception의 자식클래스
class MyException(Exception):#Exception 클래스 상속받음
    def __init__(self, e):#super로 Exception클래스를 접근
        super().__init__("{0} 으로 나눌수 없습니다.".format(e))

def division(x,y):
    if y!=0:
        return x/y
    else :
        raise MyException(y) #예외를 던져라

try:
    x=int(input())
    y=int(input())
    result=division(x,y)
    print('result : {0}'.format(result))
except MyException as e:
    print("예외 발생 : {0}".format(e))
else:
    print("정상 실행")
finally:
    print("자원 해제")

try:
    userdata=int(input())
    result=int(10/userdata)
    print('result:{0}'.format(result))
except ZeroDivisionError as e: #Exception  클래스
    print('zeroerror : {0}'.format(e))
except Exception as e: #e는 별명 
    print('exception 예외발생 : {0}'.format(e))
else: # 예외발생안했을시
    print('예외발생 안함')
finally: #자원해제용
    print("항상 실행 합니다")
