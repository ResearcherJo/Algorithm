

from collections import deque

N = int(input())

d = deque()

for i in range(N):
    T = int(input())
    if T==0:
        d.pop()
    else:
        d.append(T)
    
        
if len(d)==0:
    print('0')
else:   
    count=0
    for i in d:
        count+=i
    print(count)
    
    