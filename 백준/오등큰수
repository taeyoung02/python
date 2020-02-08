import sys
n=input()
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr_dict=dict()
stack=[0]
res=[-1]*len(arr)
for i in range(len(arr)):
    try:
        arr_dict[arr[i]]+=1
    except:
        arr_dict[arr[i]]=1

arr2=[arr_dict[arr[i]] for i in range(len(arr)) ]

for i in range(1,len(arr)):
    while stack:
        if arr2[i]>arr2[stack[-1]]:
            res[stack[-1]]=arr[i]
            stack.pop()
        else:
            break
    stack.append(i)
for i in res:
    print(i,end=' ')
    
