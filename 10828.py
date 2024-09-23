from sys import stdin

input = stdin.readline

def push(array,n):
    array.append(n)

def pop(array):
    if not array:
        return -1
    else:
        return array.pop()

def size(array):
    return len(array)

def empty(array):
    if not array:
        return 1
    else:
        return 0

def top(array):
    if not array:
        return -1
    else:
        return array[-1]

n = int(input())

array = list()

for i in range(n):
    m = input()
    if 'push' in m:
        m, n = m.split()
        n = int(n)
        push(array,n)
    elif 'top' in m:
        print(top(array))
    elif 'size' in m:
        print(size(array))
    elif 'empty' in m:
        print(empty(array))
    elif 'pop' in m:
        print(pop(array))