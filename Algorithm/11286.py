'''
풀이
https://velog.io/@babnbabn/11286%EB%B2%88-%EC%A0%88%EB%8C%93%EA%B0%92-%ED%9E%99-Python
'''
from sys import stdin

input = stdin.readline

#힙에 key값을 추가하는 함수
def insert(heap, key):
    global size
    size += 1
    current = size

    #key값이 부모보다 클때까지 올린다. 절댓값이 같다면 key값과 부모의 실제값을 비교한다.
    while current!=1 and abs(key)<=abs(heap[current//2]):
        if abs(key)==abs(heap[current//2]) and key>heap[current//2]:
            break
        heap[current] = heap[current//2]
        current//=2

    heap[current] = key

#heap의 root노드를 삭제하는 함수
def delete(heap):
    global size
    if size==0:
        return 0
    
    item = heap[1]

    temp = heap[size]
    size-=1
    parent = 1
    child = 2

    while child <= size:
        #leftchild와 rightchild중에 작은 값을 가리키게 한다. 절댓값이 같다면 실제 값을 비교한다.
        if child < size and abs(heap[child])>abs(heap[child+1]):
            child +=1
        elif child < size and abs(heap[child])==abs(heap[child+1]) and heap[child]>heap[child+1]:
            child +=1
        
        #child가 더 크다면 break한다. 절댓값이 같다면 실제 값을 비교한다.
        if abs(temp)<abs(heap[child]):
            break
        elif abs(temp)==abs(heap[child]) and temp<heap[child]:
            break

        #break가 이루어 지지 않았으면 child의 값을 올리고, child의 자식 노드로 비교한다.
        heap[parent] = heap[child]
        parent = child
        child *=2

    heap[parent] = temp
    return item

n = int(input())
size = 0
heap = [0]*100000


for i in range(n):
    key = int(input())

    if key==0:
        print(delete(heap))
    else:
        insert(heap,key)
