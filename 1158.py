from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int,input().split())

queue = deque()
array = list()

for i in range(1,n+1):
    queue.append(i)

for i in range(n):

    for j in range(k-1):
        queue.append(queue.popleft())
    
    array.append(str(queue.popleft()))

print("<",", ".join(array),">",sep='')