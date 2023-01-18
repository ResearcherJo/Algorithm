


import sys

N, K = map(int,sys.stdin.readline().split())

up = 1
down = 1
kcount=0
ncount=0
for i in range(N,0,-1):
    up*=i
    if i==K-kcount:
        down*=i
        kcount+=1
    if i==N-K-ncount:
        down*=i
        ncount+=1
    
        
print(up//down)


