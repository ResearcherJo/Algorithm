from sys import stdin

input = stdin.readline

array = list(input())
stack = list()
cnt = 0

for i in range(len(array)-1):
    if array[i] == '(':
        stack.append('(')
    else:
        if array[i-1]=='(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)