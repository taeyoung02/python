k,n=map(int,input().split())
lan=[0]*k
for i in range(k):
    lan[i]=int(input())

high=max(lan)
low=1
result=0
while low<=high:
    mid=int((high+low)/2)
    cnt=0
    for i in range(k):
        cnt+=int(lan[i]/mid)
        
    if cnt>=n:
        result=mid
        low=mid+1
    elif cnt<n:
        high=mid-1
    print("after : ", i, ", cnt : ", cnt, ", low : ", low, " mid : ", mid,", high : ",high)

print(high)



'''
4 11
802
743
457
539
'''

