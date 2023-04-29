from sys import stdin

input = stdin.readline

def insert(heap, key):
    global size
    size += 1
    current = size

    while current!=1 and abs(key)<=abs(heap[current//2]):
        if abs(key)==abs(heap[current//2]) and key>heap[current//2]:
            break
        heap[current] = heap[current//2]
        current//=2

    heap[current] = key

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
        if child < size and abs(heap[child])>abs(heap[child+1]):
            child +=1
        elif child < size and abs(heap[child])==abs(heap[child+1]) and heap[child]>heap[child+1]:
            child +=1
        
        if abs(temp)<abs(heap[child]):
            break
        elif abs(temp)==abs(heap[child]) and temp<heap[child]:
            break

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
