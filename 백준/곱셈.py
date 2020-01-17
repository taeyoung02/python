import sys
A,B,C=map(int,input().split())

def requr(b):
    if b==0:
        return 1
    temp=requr(int(b/2))
    result=(temp*temp)%C
    if b%2:#b가 0이 될때까지 나누고 temp=1이되어 제일밑까지 내려간후 b는 다시 1로 올라감
        result=result*A%C
    return result#A를 반환후 b는 2의 배수로 증가하며 result에 1*1 , 2*2, 4*4이런식으로 B에 가까워짐
    
print(requr(B))

    
    
