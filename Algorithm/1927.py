from sys import stdin

input = stdin.readline

#heap에 key를 삽입하는 함수 / heap : heap, key : key값
def insert(heap, key):
    global size
    size += 1
    current = size

    #key값을 heap의 마지막에 넣어놓고, 부모랑 비교해서 부모가 더 크다면 올린다.
    while current!=1 and key < heap[current//2]:
        heap[current] = heap[current//2]
        current//=2

    heap[current] = key

#heap에서 root를 삭제한다. / heap : heap
def delete(heap):
    global size
    #size가 0이면 0을 출력
    if size==0:
        return 0
    
    #root를 출력한다.
    item = heap[1]

    #heap의 가장 마지막 값을 root로 올린다.
    temp = heap[size]
    size -= 1

    parent = 1
    child = 2

    while child <= size:
        #leftchild인지 rightchild인지 결정한다. rightchild가 더 작다면 child가 rightchild를 가리키게 한다.
        if child < size and heap[child+1]<heap[child]:
            child += 1

        #temp가 child보다 작다면 parent자리에 넣으면 되기때문에 break
        if temp < heap[child]:
            break

        #아래 있던거를 올리고, temp를 아래로 내려서 다시 비교한다.
        heap[parent] = heap[child]
        parent = child
        child *= 2

    heap[parent] = temp
    return item


n = int(input())
heap = [0] * 100000
size = 0 #heap에 들어가 있는 원소 갯수

for _ in range(n):
    x = int(input())
    
    if x==0:
        print(delete(heap))
    else:
        insert(heap,x)