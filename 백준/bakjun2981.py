n=int(input())
a=[None]*n
for i in range(n):
    a[i]=int(input())

def gcd(x,y):
    if y==0:
        return x
    mod=x%y
    return gcd(y,mod) #재귀함수사용시 리턴이 필수

GCD=abs(a[1]-a[0])

for i in range(1,n-1):
    GCD=gcd(GCD,abs(a[i+1]-a[i]))
result=[]
for i in range(2,int(GCD**(1/2))+1):
    if not GCD%i:
        result.append(i)
        result.append(int(GCD/i))
result.append(GCD)
result=list(set(result))
result.sort()
for i in result:
    print(i,end=' ')