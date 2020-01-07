#list, dictionary, set는 mutable 가능 ( 함수에서의 변경이 저장됨 ) 포인터이기 때문

def outer_func(func):
    res=0
    def inner_func(*args, **kwargs): # *로 튜플을 받고 **로 딕셔너리를 받는다. 포인터로 여러 요소를 한번에 받을수있다
        print("func name =", func.__name__)
        print("args=",args)
        print("kwargs=",kwargs)
        nonlocal res #바깥함수의 변수를 안쪽함수에서 변경하면 새로운 변수가 선언되는데,
                     #nonlocal을 이용하면 바깥함수의 변수를 변경할수있다
        res = func(*args, **kwargs)
        print("res=",res)
        return res
    return inner_func

def add(a,b,**info): #integer와 **kwargs를 받는다
    for key, value in info.items():
        print("{} , {}".format(key,value),end='   ') #end로 마지막을 마음대로
    return a+b

f=outer_func(add) #f에 outer_func(add) 저장
print('\n')
result = f(2,3,taeyoung = 40, zayoung = 60) #args에 2,3  kwargs에 뒤에 저장
print('\n')
print(result)
#res=func()실행되어 add(a,b,**info)실행
#키와 밸류 출력후 a+b리턴
#res에 5저장
#res를 return하며 inner_func종료
#inner_func(res)를 return하며 outer_func종료
#result에 5저장