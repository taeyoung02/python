n,k=map(int,input().split())
arr=[]
arr=list(range(1,n+1))

i=k-1
result=[]
for _ in range(n):
    i%=len(arr)
    result.append(str(arr.pop(i)))
    i+=k-1
print(result)
print("<"+', '.join(result)+">") #join은 리스트를 문자열로 만드는데 리스트안에 있는 요소도 문자열이어야함

    