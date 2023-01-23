from collections import deque
from sys import stdin

input = stdin.readline

N = int(input())

deq = deque()

for i in range(N):
    S = input()
    
    if 'push_front' in S:
        S, T = S.split()
        T = int(T)
        deq.appendleft(T)
    elif 'push_back' in S:
        S, T = S.split()
        T = int(T)
        deq.append(T)
    elif 'pop_front' in S:
        if not deq:
            print('-1')
        else:
            print(deq.popleft())
    elif 'pop_back' in S:
        if not deq:
            print('-1')
        else:
            print(deq.pop())
    elif 'size' in S:
        print(len(deq))
    elif 'empty' in S:
        if not deq:
            print('1')
        else:
            print('0')
    elif 'front' in S:
        if not deq:
            print('-1')
        else:
            print(deq[0])
    else:
        if not deq:
            print('-1')
        else:
            print(deq[-1])