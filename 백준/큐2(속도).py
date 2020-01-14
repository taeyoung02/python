import sys
test=int(sys.stdin.readline().rstrip())
arr=[]
k=0
for i in range(test):
    order=sys.stdin.readline().rstrip().split()
    if order[0]=="push":
        arr.append(int(order[1]))
    elif order[0]=="pop":
        if k>=len(arr):
            print(-1)
            continue
        print(arr[k])
        k+=1
    elif order[0]=="size":
        print(len(arr)-k)
    elif order[0]=="empty":
        if len(arr)-k==0:
            print(1)
        else: print (0)
    elif order[0]=="front":
        if len(arr)-k==0:
            print(-1)
            continue
        print(arr[k])
    elif order[0]=="back":
        if len(arr)-k==0:
            print(-1)
            continue
        print(arr[-1])