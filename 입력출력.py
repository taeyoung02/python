#입력은 기본적으로 문자열로 저장되기 때문에 형변환이 필요
import math
langs = ["korean", "english"]

for s ,i in enumerate(langs, start=1):
    print("{}. {}".format(s,i))

while True:
    sellect = input("choose language : ")
    if not sellect.isnumeric():
        continue
    sellect=int(sellect)
    if 0< sellect <3:
        break

print("{}".format(langs[sellect-1]))

#에라토스테네스의 체

prime=[]
num=int(input("input the number : "))
prime_check=[False, False]+[True]*(num-1)

for i in range(2, int(math.sqrt(num)+1)):
    if prime_check[i]:
        for j in range(2*i,num+1, i):
            prime_check[j]=False

prime=[i for i in range(2,num+1) if prime_check[i]]

print(prime)

if num in prime : print("yes")
else : print("no")