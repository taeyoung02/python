n=int(input())
arr=[(0,0) for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    arr[i]=(a,b)
arr.sort()
d=[]
a=0
d.append(arr[0])
for i in range(1,n):
    if d[a][1]>arr[i][1]: #전의 끝나는시간보다 끝나는시간이 앞일때
        d[a]=arr[i]
    elif d[a][1]<=arr[i][0]:
        d.append(arr[i])
        a+=1
    else: pass
print(len(d))