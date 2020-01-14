import sys 
size,n = map(int,sys.stdin.readline().rstrip().split())

arr=[]
for i in range(size):
    arr.append(i+1)
target=list(map(int,sys.stdin.readline().split()))
cnt=0
while len(target)>0:
    if arr[0]==target[0]:
        arr.pop(0)
        target.pop(0)
    else:
        if arr.index(target[0])>len(arr)/2:
            arr.insert(0,arr.pop(-1))
            cnt+=1
        else:
            arr.append(arr.pop(0))
            cnt+=1
print(cnt)