from sys import stdin

input = stdin.readline

n = int(input())

for i in range(n):
    string = list(input())
    stack = list()
    for i in string:
        if i =='(': 
            stack.append('(')
        elif i==')' and stack:
            stack.pop()
        elif i==')' and not stack: # ) 인경우인데 스택이 비어있다면 NO를 출력
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
