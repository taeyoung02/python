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
