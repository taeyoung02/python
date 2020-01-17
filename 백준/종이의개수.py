import sys
n=int(sys.stdin.readline().rstrip())
arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
sum=[0]*3
def requr(x,y,n):
    if n==0:
        return
    point = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if point != arr[i][j]:
                n=int(n/3)
                for i in range(3):
                    for j in range(3):
                        requr(x+n*i,y+n*j,n)
                return
    sum[point+1]+=1
   
requr(0,0,n)
for i in range(3):
    print(sum[i])