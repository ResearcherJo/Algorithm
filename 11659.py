import sys


n1, n2 = map(int,sys.stdin.readline().split())

nl = list(map(int,sys.stdin.readline().split()))

for i in range(1,n1):
    nl[i] = nl[i]+nl[i-1]
    
for i in range(n2):
    s, f = map(int,sys.stdin.readline().split())
        
    if s!=1:
        result = nl[f-1] - nl[s-2]
    else:
        result = nl[f-1]
    
    print(result)