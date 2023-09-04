import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int,input().split())

campus = [list(input().strip()) for _ in range(n)]

queue = deque()
count = 0 

def dfs(campus, i,j):
    global count
    if campus[i][j] == 'X':
        return

    campus[i][j] = 'X' #방문 했음을 알리는 것

    #상하좌우 순으로 보면서 탐색
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if x<m and x>=0 and y<n and y>=0: #배열 끝을 넘지 않게
            if campus[y][x] == 'O':
                dfs(campus, y, x)
            elif campus[y][x] == 'P':
                count+=1
                dfs(campus, y,x)

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I' :
            dfs(campus,i,j)
            break

if count==0:
    print('TT')
else:
    print(count)
