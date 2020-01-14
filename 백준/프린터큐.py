test=int(input())
for i in range(test):
    n,m=map(int, input().split())
    arr=list(map(int, input().split()))
    
    target=arr[m]
    queue=sorted(arr)
    queue.reverse()
    target+=0.5
    arr[m]+=0.5
    cnt=1
    while True:
        if int(arr[0])==queue[0]:
            if arr[0]==target:
                print(cnt)
                break
            arr.pop(0)
            queue.pop(0)
            cnt+=1
        else:
            arr.append(arr.pop(0))