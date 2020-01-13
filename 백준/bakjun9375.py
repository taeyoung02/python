n=int(input())
for i in range(n):
    arr=dict()
    num=int(input())
    for i in range(num):
        a=input().split()
        if a[-1] in arr:
            arr[a[-1]]+=1
        else :
            arr[a[-1]]=1
    ans=1
    for values in arr.values():
        ans*=(values+1)
    print(ans-1)

