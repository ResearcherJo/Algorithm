

import sys

n, m = map(int,input().split())

l=dict()
kg=dict()

for i in range(n):
    e = sys.stdin.readline().strip()
    l[i]=e
    kg[e] = i


for i in range(m):
    k = sys.stdin.readline().strip()
    if k.isdecimal():
        print(l[int(k)-1])
    else:
        print(kg[k]+1)
        
'''
    딕셔너리는 해시라서 빠르다. 딕셔너리로 할 수 있으면 하는게 좋다. 그래야 시간초과 잘 안나요...
'''