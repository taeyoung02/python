import eratostenes
c = 10
def mul(a,b):
    global c #전역변수 c를 사용하겠다
    c=a*b
    return c

print("mul={}, c={}".format(mul(2,3),c))

def get_input_user(msg):
    user = input(msg) #msg가 출력되고 입력을 받음
    return user #입력된 문자열 리턴
user=get_input_user("input the name : ") #함수가 실행뒤 user에 저장
print(user)

def get_user_data(msg,cast=str): #디폴트값
    while True:
        try:
            user = cast(input(msg)) #msg출력후 입력받은것을 형변환 만약 int가 
            return user
        except:
            continue

#user_age= get_user_data("input the user age>",int)
#user_name=get_user_data("input the user name>")

num=get_user_data("input the numver over 2>",int)
eratostenes.eratostenes(num)

a=ord(input()) #문자열을 받은뒤 문자를 아스키코드값으로 변환하는 함수를 사용
#ord함수는 문자한개를 받는다.
b=chr(int(input())) #입력을 받을때 "97"처럼 문자열이 들어오는데, 이를 int형으로 바꾸면 97이 된다.
# chr을 이용하면 숫자를 받아 문자로 돌려주는데
# 문자열"97"은 숫자가 아니라 문자열이기 때문에 chr(input())은 동작하지않는다
# 문자열 "97"을 int로 형변환 해줘야 chr함수에 숫자가 들어가서 문자를 반환한다
print(a)
print(b)
print(ord(b))# 문자를 다시 숫자로
def save_winner(*args):
    print(args)

save_winner(input())

def save_winner2(**kwargS):
    '''
    explain
    '''       #docstring : 함수에 커서를 대면 표시됨
    print(kwargS)
    if kwargS.get("neme"):
        print(kwargS["nema"])
    else:
        print(kwargS["name"])

save_winner2(name="taeyoung",nema="gimoddi")

hello = save_winner #hello변수에 함수저장
hello(input()) #함수실행
print(type(hello)) 

def add(a, b):
    return a+b

def function1(func,a,b):
    print("{}".format(func(a,b))) #함수안에 함수를 실행시킨다

function1(add,2,4) #첫번째 인자로 함수를 받음