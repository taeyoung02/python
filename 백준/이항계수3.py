# n C k = n! / k!(n-k)!
# n C k를 1000000007로 나눈 나머지를 구하라 (n,k는 매우큼)
n,k=map(int,input().split())
fac=[1]*4000001
p=1000000007
for i in range(2,4000001):#N!%p
    fac[i]=(fac[i-1]*i)%p

def requr(n,k):#N!의K제곱 % P
    if k==0:
        return 1
    temp=requr(n,int(k/2))
    result=temp*temp%p
    if k%2:
        result*=n
    return result%p
print((((fac[n]*requr(fac[n-k],p-2))%p)*(requr(fac[k],p-2))) %p)


'''
페르마의 소정리

a**(p-1)=1 (mod p)

a**(p-2)=a**-1 (mod p)

[n! / k!(n-k)!] (mod p) = [n! * ( k!(n-k)! )**(p-2)] (mod p)

= [n! * k!**(p-2)(mod p) * (n-k)!**(p-2)(mod p)]