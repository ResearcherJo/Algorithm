from collections import deque

T = int(input())


for i in range(T):
    L = input()
    deq = deque()
    for i in L:
        if i=='(' or i=='[':
            deq.append(i)
        elif (i==']' or i==')'):
            if len(deq)==0:
                print('NO')
                break
            elif (i==']' and deq.pop()!='[') or (i==')' and deq.pop()!='('):
                print('NO')
                break
    else:
        if len(deq)==0:
            print('YES')
        else:
            print('NO')