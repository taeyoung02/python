a = [[[1,2],[3,4],[5,6]]]
for i in a:
    for j in i:
        for k in j:
            print(k)

student = [{'yoon':12}, {'tae':20},{'young':30}]


for s, i in enumerate(student, start=0):
    data = (list(i.items())[0])
    name = data[0]
    number=data[1]
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