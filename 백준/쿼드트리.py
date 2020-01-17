n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
def requr(x,y,n):
    if n==0:
        return
    point = arr[x][y]
    state=True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if point != arr[i][j]:
                state=False
    if state:
        print(point,end="")
    else:
        print("(",end="")
        requr(x,y,int(n/2))
        requr(x,y+int(n/2),int(n/2))
        requr(x+int(n/2),y,int(n/2))
        requr(x+int(n/2),y+int(n/2),int(n/2))
        print(")",end="")
requr(0,0,n)