

import sys


n, m = map(int,sys.stdin.readline().split())

d = dict()

for i in range(n):
    a, p = sys.stdin.readline().split()
    
    d[a]=p
    
    
for i in range(m):
    print(d[sys.stdin.readline().strip()])