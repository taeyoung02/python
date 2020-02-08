class carMixIN:
    def ready(self):
        print("믹스인레디")
    def start(self):
        print("{} 가 {} 속도로 달립니다".format(self.name, self.speed))

class Performance():
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed
        self.ready()#믹스인. 자식클래스에 연결된 부모클래스끼리 함수공유가능

class superCar(carMixIN, Performance):
    def show_info(self):
        print("{}는 {}속도의 성능입니다".format(self.name, self.speed))

    def start(self):#오버라이딩
        super().start()#부모클래스를 씀(super.__init__ 부모생성자 실행)
        print("스타트")

s=superCar("람보르",300)
s.show_info
s.start()