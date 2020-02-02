class fishcake:
    def __init__(self,**kwargs):#생성자
        self._size=10
        self._flavor="pot"
        self._price=100
        if "size" in kwargs:
            self._size=kwargs.get("size")
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")
    def __del__(self):#소멸자
        print("delete complete")

    def __str__(self): #클래스가 print에 의해 출력될 때 발생
        return "<class fishcake (size={}, price={}, flavor={})".format(self._size,self._price,self._flavor)
    
    def show(self):
        print("~~~")
    
class market(fishcake): #상속
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)#????
        self._market_price=self._price+margin
    def show(self):
        print(self._flavor, self._market_price)

def add(a,b):
    return a+b

if __name__ == "__main__":
    objefish = fishcake()
    objefish2 = fishcake(size="big", price=10, flavor="sucreame")
    print(objefish)
    print(objefish2)
    _market=market(price=100)
    _market.show()