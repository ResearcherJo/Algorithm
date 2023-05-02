from sys import stdin

input = stdin.readline

def insert_min(minheap,key):
    global size
    size+=1
    current = size

    while current!=1 and key<minheap[current//2]:
        minheap[current] = minheap[current//2]
        current//=2
    
    minheap[current] = key


def insert_max(maxheap,key):
    global size
    size+=1
    current = size

    while current!=1 and key>maxheap[current//2]:
        maxheap[current] = maxheap[current//2]
        current//=2
    
    maxheap[current] = key

def delete_min(minheap, maxheap):
    global size
    
    if size == 0:
        return

    item = minheap[1]
    size-=1

    temp = minheap[size]
    parent = 1
    child = 2

    while  child <=size:
        if child < size and minheap[child]>minheap[child+1]:
            child += 1

        if temp < minheap[child]:
            break

        minheap[parent] = minheap[child]
        parent = child
        child*=2

    minheap[parent] = temp
    return item


def delete_max(maxheap, minheap):
    global size
    
    if size == 0:
        return False

    item = maxheap[1]
    size-=1

    temp = maxheap[size]
    parent = 1
    child = 2

    while  child <=size:
        if child < size and maxheap[child]<maxheap[child+1]:
            child += 1

        if temp > maxheap[child]:
            break

        maxheap[parent] = maxheap[child]
        parent = child
        child*=2
    maxheap[parent] = temp
    return item



minheap = [-1] * 1000001
maxheap = [-1] * 1000001
delete = dict()

t = int(input())

for _ in range(t):
    k = int(input())
    size = 0
    for _ in range(k):
        c, n = input().split()
        if c == 'D':
            if n == '-1':
                while True:
                    m = delete_min(minheap,maxheap)
                    if m and delete[m]>=1:
                        delete[m] -=1
                        break


            else:
                while True:
                    m = delete_max(minheap,maxheap)
                    if m and delete[m]>=1:
                        delete[m] -=1
                        break
        else:
            n = int(n)
            if n in delete:
                delete[n] +=1
            else:
                delete[n] = 0
            insert_max(maxheap,n)
            size-=1
            insert_min(minheap,n)
        #print('maxheap : {}, minheap : {}'.format(maxheap[1], minheap[1]))
        #print('size : {}'.format(size))
    if size==0:
        print('EMPTY')
    else:
        if size>=2:
            ma = delete_max(maxheap,minheap)
            mi = delete_min(minheap,maxheap)
            print(ma,mi)
        else:
            item = delete_max(maxheap,minheap)
            print(item,item)
