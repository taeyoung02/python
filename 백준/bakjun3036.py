n=int(input())
a=list(map(int, input().split()))#list에 문자열 쪼개서 각각 숫자로 저장함
def gcd(a,b):
    if b==0:
        return a
    mod=a%b
    return gcd(b,mod)

for i in range(1,n):
    print("{}/{}".format(int(a[0]/gcd(a[0],a[i])), int(a[i]/gcd(a[0],a[i]))))
