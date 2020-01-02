from sys import stdin
n=int(stdin.readline().strip())
a=list(map(int, stdin.readline().split(" ")))
d=[0] * n
d[0]=a[0]
for i in range(1,len(a)):
    d[i]=max(d[i-1]+a[i],a[i])
d.sort()
d.reverse()
print(d[0])

