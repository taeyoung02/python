#a의 요소의 값이 바뀌는데 a에 구간 r~l까지의 합을 알고싶을때, lgN만에 구할수있다 
import math
import sys
n,m,k=map(int,sys.stdin.readline().rstrip().split())
a=[0]*n
for i in range(n):
    a[i]=int(sys.stdin.readline().rstrip())
#트리에 a배열의 구간합을 저장하는데 리프노드는 a의 원소를 가진다
tree=[0]*(2**(math.ceil(math.log(n,2))+1))
#트리크기를 2N개로하면 트리를 배열로만들기 때문에 배열의 빈공간은 트리에 나타나지않는다
#따라서 전체노드개수가 2*N-1이지만 트리를 배열에 옮기게 되면 풀트리로 상정해야한다
#a의 개수 = tree 리프노드 개수
#2**(math.ceil(logN) + 1)-1의 공간이 필요하다 (트리의 높이 = log(리프노드개수)+1)



def init(a, tree, node, start, end):#배열 a, 세그먼트 트리, 노드번호, start~end : 노드가 담당하는 합의범위
    if start==end:#리프노드일때(함수가 계속호출되어 start=end가 되고, 그만큼 node도 2배씩 커져서 끝까지 내려가게됨)
        tree[node]=a[start]
        return tree[node]
    else:
        tree[node]=init(a, tree, node*2, start,int((start+end)/2))+\
            init(a, tree, node*2+1, int((start+end)/2+1), end)
        return tree[node]
#left~right의 합을 구하고싶다
def sum(tree, node, start, end, left, right):
    if left>end or right<start: #겹치지 않을때
        return 0
    elif left<=start and end<=right:#start~end가 left~right포함
        return tree[node]
    else: #left~right가  start~end를 포함하거나 서로 겹칠때
        result=sum(tree, node*2, start, int((start+end)/2), left, right)+\
            sum(tree, node*2+1, int((start+end)/2+1), end, left, right)
        return result

#a의 값을변경할때.  세그먼트 트리에 포함되는 구간을 다 바꿔줘야함 
def update(tree, node, start, end, index, diff):#diff = val-a[index] 인덱스 번째의 값을 val로 수정
    if index<start or index>end :#구간에 없을때 종료
        return
    tree[node] = tree[node]+diff
    if start!=end:#리프노드가 아니면 자식도 변경해야하기 때문에 재귀로 계속 내려감
        update(tree, node*2, start, int((start+end)/2), index, diff)
        update(tree, node*2+1, int((start+end)/2+1), end, index, diff)

sys.setrecursionlimit(100000)
init(a, tree, 1, 0, n-1)

for _ in range(m+k):
    order=list(map(int,sys.stdin.readline().rstrip().split()))
    if order[0]==1:
        update(tree, 1, 0, n-1, order[1]-1, order[2]-a[order[1]-1])
        a[order[1]-1]=order[2]
    elif order[0]==2:
        print(sum(tree,1,0,n-1,order[1]-1,order[2]-1))