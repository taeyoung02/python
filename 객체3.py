#Abstract class 추상 클래스
from abc import ABCMeta
from abc import abstractmethod #모듈과 패키지
class sex(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod #자식클래스가 이 함수를 반드시 재정의 해야함
    def printAt2(self):
        print("sex")

class ParentClass:

    def __init__(self):
        self.at1='python'#부모 클래스의 속성, init method는 자식클래스에서 자동으로 호출이안됌
        self.at2='c++' #자식클래스의 메모리에 초기화되지않음

    def printMethod(self):
        print("Hello python")

    def printAt(self):
        print(self.at1)
        print(self.at2)


class childClass(ParentClass, sex):#다중상속

    def __init__(self):
        ParentClass.__init__(self) #자식클래스 init method에 호출시켜야함
        #혹은
        #super().__init__() #super가 위쪽을 가리키기 때문에 self 필요없음
    def printAt2(self):
        print("noSex")#오버라이딩


ChildCls=childClass()
ChildCls.printMethod()
ChildCls.printAt()
ChildCls.printAt2()



