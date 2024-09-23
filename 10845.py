from sys import stdin

input = stdin.readline

def push(array, n):
    array.append(n)

def pop(array):
    if array:
        return array.pop(0)
    else:
        return -1

def size(array):
    return len(array)

def empty(array):
    if array:
        return 0
    else:
        return 1

def front(array):
    if array:
        return array[0]
    else:
        return -1

def back(array):
    if array:
        return array[-1]
    else:
        return -1

n = int(input())
array = list()

for i in range(n):
    
    m = input().split()

    if 'push' in m:
        push(array,int(m[-1]))
    elif 'pop' in m:
        print(pop(array))
    elif 'size' in m:
        print(size(array))
    elif 'empty' in m:
        print(empty(array))
    elif 'front' in m:
        print(front(array))
    elif 'back' in m:
        print(back(array))
