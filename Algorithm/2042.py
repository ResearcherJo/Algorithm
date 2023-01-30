from sys import stdin

input = stdin.readline

#트리 생성
def init(tree, array, node, start, end): 
    if start == end:
        tree[node] = array[start]
        return tree[node]

    mid = (start + end)//2

    tree[node] = init(tree,array,node*2,start, mid) + init(tree, array, node*2+1, mid+1, end)
    return tree[node]

#트리 수정
def update(tree, node, start, end, index, dif):
    if not(start<=index and index<=end):
        return

    tree[node] += dif

    if start != end : #끝이 아니면 더 내려가야 하기 때문에
        mid = (start + end)//2
        update(tree, node*2, start, mid, index, dif)
        update(tree, node*2+1, mid+1, end, index, dif)

#부분합 구하기
def sum(tree, node, start, end, left, right): #left ~ right 구간의 합을 구하고자 한다.
    if right<start or end<left: #start~end가 left~right범위에 포함되지 않는 경우
        return 0

    if left <= start and end <= right: #left~right가 start~end를 포함하는 경우
        return tree[node]

    # start~end가 left~right를 포함하는 경우, 나머지 경우(left<=start<=right<=end)
    mid = (start + end)//2
    return sum(tree, node*2, start, mid, left, right) + sum(tree, node*2+1, mid+1, end, left, right)


n, m, k = map(int,input().split())

array = [int(input()) for i in range(n)]
tree = [0]*3000000

init(tree, array, 1, 0, len(array)-1)

for i in range(m+k):
    a, b, c = map(int,input().split())

    if a==1:
        update(tree, 1, 0, n-1, b-1, c-array[b-1])
        array[b-1] = c #array의 값도 바꿔 놓아야 한다.
    elif a==2:
        print(sum(tree, 1, 0, n-1, b-1, c-1))