a = [[[1,2],[3,4],[5,6]]]
for i in a:
    for j in i:
        for k in j:
            print(k)

student = [{'yoon':12}, {'tae':20},{'young':30}]

print(type(student[0].items()))#<class 'dict_items'>형

for s, i in enumerate(student, start=0):
    data = list(i.items())[0]#i.items()=student[0].items() 이고 리스트로 형변환해주면 [('yoon', 12)]를 반환한다.
                            # 리스트형식이므로 0번째 요소를 가져오면 튜플이 남는다
    name = data[0] #튜플의 0번째
    number=data[1] #1번째
    print("{} name={}, number={}".format(s,name,number))

result=[]
for i in range(4):
    result.append(i+3)
print(result)
#comprehension
result=[num+5 for num in range(0,4)]
print(result)

result=[num*3 for num in range(1,20) if num%2==0]
print(result)

gugudan= ["{} x {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
print(gugudan)

point = [30,70,90]
for p in point:
    if p<70:
        continue
    if p>80:
        break
    print("{}".format(p))