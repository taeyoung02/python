import sys
n=input()
arr=list(map(int,sys.stdin.readline().rstrip().split()))
stack=[0]
res=[-1]*len(arr)
for i in range(1,len(arr)):
    while stack:
        if arr[i]>arr[stack[-1]]:
            res[stack[-1]]=arr[i]
            stack.pop()
        else:
            break
    stack.append(i)
for i in res:
    print(i,end=' ')
