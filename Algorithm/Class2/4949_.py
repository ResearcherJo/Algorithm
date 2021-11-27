

from collections import deque


while True:
    L = input()
    deq = deque()
    if L=='.':
        break
    for i in L:
        if i=='(' or i=='[':
            deq.append(i)
        elif (i==']' or i==')'):
            if len(deq)==0:
                print('no')
                break
            elif (i==']' and deq.pop()!='[') or (i==')' and deq.pop()!='('):
                print('no')
                break
    else:
        if len(deq)==0:
            print('yes')
        else:
            print('no')
        
'''
    스택에서의 조건 스택에 있는 요소의 수 같은걸 좀 빼먹었었다.
'''