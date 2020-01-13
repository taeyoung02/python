a=input()
before=0
arr=[]
for i in range(len(a)):
    if not a[i].isnumeric():
        arr.append(int(a[before:i]))
        before=i
arr.append(int(a[before:]))
arr2=[]

for k in range(len(arr)):
    if arr[k]<0:
        sum=0
        sum-=arr[k]
        while  k+1 < len(arr) and arr[k+1]>0:
            k+=1
            sum+=arr[k]
        arr2.append(-sum)
    else:
        arr2.append(arr[k])
    k+=5
result=0
print(arr2)
for i in arr2:
    result+=i
print(result)           