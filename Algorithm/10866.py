

from collections import deque
import sys


N = int(input())

deq = deque()

for i in range(N):
    S = sys.stdin.readline()
    
    if 'push_front' in S:
        S, T = S.split()
        T = int(T)
        deq.appendleft(T)
    elif 'push_back' in S:
        S, T = S.split()
        T = int(T)
        deq.append(T)
    elif 'pop_front' in S:
        if len(deq)==0:
            print('-1')
        else:
            print(deq.popleft())
    elif 'pop_back' in S:
        if len(deq)==0:
            print('-1')
        else:
            print(deq.pop())
    elif 'size' in S:
        print(len(deq))
    elif 'empty' in S:
        if len(deq)==0:
            print('1')
        else:
            print('0')
    elif 'front' in S:
        if len(deq)==0:
            print('-1')
        else:
            print(deq[0])
    else:
        if len(deq)==0:
            print('-1')
        else:
            print(deq[-1])
    
    
'''
    시간초과 났을때는 sys.stdin.readline을 써보자
'''