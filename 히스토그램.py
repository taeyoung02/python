import sys
import math
#막대기의 높이가 정렬되어 있지않기때문에 이진탐색은 쓸수없다.

#따라서 각 구간의 최소값을 저장해놓은 세그먼트 트리를 사용해야한다
#루트노드: 0~n-1까지의 최소높이
#리프노드: 각각의 요소들(0,1...n-1)
def init(a, tree, node, start, end):#배열 a, 세그먼트 트리, 노드번호, start~end : 노드가 담당하는 합의범위
    if start==end:#리프노드일때(함수가 계속호출되어 start=end가 되고, 그만큼 node도 2배씩 커져서 끝까지 내려가게됨)
        tree[node]=start
    else:
        init(a, tree, node<<1, start,int((start+end)>>1))
        init(a, tree, (node<<1)+1, int(((start+end)>>1)+1), end)
        tree[node]= (lambda x ,y: x if a[x]<a[y] else y) (tree[node<<1],tree[(node<<1)+1])
        

#구간에서 제일 작은 값을 찾음(h의)
#left와 right는 우리가 구하고싶은 구간
def query(a, tree, node, start, end, left, right):
    #구간에 포함이안되면 제낀다. 즉 트리의 노드의 구간이 left, right구간과 겹치지 않는다
    if left>end or right<start: #겹치지 않을때
        return -1
    #구간에 포함되면, 즉 구하고자하는 범위안에 세그먼트 트리의 노드(h의 구간의 최소값)가 있으면
    #그 노드를 반환
    if start>=left and end<=right:#left~right안에 start~end있음
        return tree[node] #트리의 값 반환: a의 구간에서의 최소값 반환

    #노드번호가 증가하며 구간을 감소해 나가는데, 각 노드는 일정한 구간을 갖게된다(start와 end사이)
    m1 = query(a,tree,node<<1,start, int((start+end)>>1), left, right)
    m2 = query(a,tree,(node<<1)+1,int((start+end)>>1)+1,end,left,right)
    if m1==-1:
        return m2
    elif m2==-1:
        return m1
    else:
        if a[m1] <=a[m2]:
            return m1
        else:
            return m2

#제일큰 직사각형넓이 갱신
def largest(a, tree, start, end):
    stack,max_area=[(start,end)],0
    n=len(a)
    while stack:
        start,end=stack.pop()
        if start==end:
            if a[start]>max_area:
                max_area=a[start]
        else:
            m=query(a,tree,1,0,n-1,start,end)
            area=(end-start+1)*a[m]
            if area>max_area:
                max_area=area
            if start<m:
                stack.append((start,m-1))
            if end>m:
                stack.append((m+1,end))
       
    return max_area
sys.setrecursionlimit(10000)
while True:
    temp=list(map(int,input().split()))
    n=temp[0]
    h=temp[1:]
    if n==0:
        exit(0)
    tree=[0]*(2**(math.ceil(math.log(n,2))+1))#트리인덱스 1부터시작
    init(h,tree,1,0,n-1)
    print(largest(h,tree,0,n-1))