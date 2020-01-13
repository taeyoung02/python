n=int(input())
a=[]
stack=[]
for i in range(n):
    a.append(int(input()))

k=0
ans=[]
for i in range(n):
    ans.append('+')
    stack.append(i+1)
    while stack and k<n:
        if stack[-1]==a[k]:
            stack.pop()
            ans.append('-')
            k+=1
        else : break
if not stack:
    for i in ans:
        print(i)
else:
    print('NO')



