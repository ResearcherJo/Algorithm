

import sys


N = int(input())

l = list()

for i in range(N):
    l.append(list(map(int,sys.stdin.readline().split())))
    
l.sort(key = lambda x: x[0])
l.sort(key = lambda x: x[1])

for i in l:
    print(i[0], i[1])
    
    
    