test=int(input())
for _ in range(test):
    order=input()
    n=int(input())
    arr=input()
    if arr=="[]": arr=[]
    else: arr=arr[1:-1]; arr=list(map(int,arr.split(',')));
    Rcnt=0
    k=0
    state=0
    while len(order)-k>0:
        if order[k]=='R':
            Rcnt+=1
            k+=1
        elif order[k]=='D':
            if len(arr)==0:
                print("error")
                state=1
                break
            if Rcnt%2:#Rcnt가 홀수면
                arr.pop(-1)
            else:
                arr.pop(0)
            k+=1
    if state:
        continue
    if Rcnt%2:
        arr.reverse()
        print("["+",".join(map(str,arr))+"]")
    else: print("["+','.join(map(str,arr))+"]")
