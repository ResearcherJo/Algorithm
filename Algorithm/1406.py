'''
from sys import stdin,stdout

input = stdin.readline
print = stdout.write

array = list(input().strip())
point = len(array)

n = int(input())

for i in range(n):
    S = input()
    if 'P' in S:
        a, s = S.split()
        array.insert(point,s)
        point+=1
    elif 'L' in S:
        if point != 0:
            point -=1
    elif 'D' in S:
        if point != len(array):
            point +=1
    elif 'B' in S: 
        if point != 0:
            array.pop(point)
            point -=1
    
print("".join(map(str,array)))
'''


























'''
from sys import stdin

input = stdin.readline

L = list(input().rstrip())
R = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
            if L: #L이 비어있다는 것은 가장 왼쪽이라는 소리이기 때문에 왼쪽으로 못가게 해야 한다.
                R.append(L.pop())
    elif command[0] == 'D':
        if R: #R이 비어있다는 것은 가장 오른쪽이라는 소리이기 때문에 오른쪽으로 못가게 해야 한다.
            L.append(R.pop())
    elif command[0] =='B':
        if L:
            L.pop()
    else:
        L.append(command[1])

L.extend(reversed(R)) #reverrse가 아닌 reversed인 이유는 R이 비어 있을때 오류가 나지 않기 위해서이다.
print(''.join(L))
'''