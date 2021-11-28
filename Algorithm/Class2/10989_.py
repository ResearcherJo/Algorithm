

import sys

N = int(input())

L = [0 for _ in range(10001)]

for i in range(N):
    
    L[int(sys.stdin.readline().strip())]+=1
    
for i in range(len(L)):
    if L[i]!=0:
        for j in range(L[i]):
            print(i)
            
'''
    메모리초과 시간초과 나면 python3 나 pypy3를 번갈아 시도해보고 다른 방식으로도 풀어봐야 겠다.
'''