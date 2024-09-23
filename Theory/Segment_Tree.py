

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