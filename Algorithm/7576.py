from sys import stdin
from collections import deque

input = stdin.readline

dx = [1,0,-1,0]
dy = [0,-1,0,1]
queue = deque()

#토마토가 있는 곳을 queue에 넣어준다.
def init(array, n, m):
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                queue.append([j,i])


def bfs(array, m, n):
    while queue:
        now = queue.popleft()
        
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if next_x>=0 and next_x<m and next_y>=0 and next_y<n: #토마토 창고 넘어가지 않게 
                if array[next_y][next_x] == 0: #토마토가 있다면
                    array[next_y][next_x] = array[now[1]][now[0]] + 1 #옮겨 갈 곳은 지금 있는 곳보다 1일 뒤일 것이다.
                    queue.append([next_x,next_y])



m, n = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
boo = False
count = 0

init(array,n,m)
bfs(array,m,n)

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            boo = True
            break
    if boo:
        break

if boo:
    print(-1)
else:
    mx = 0
    for i in array:
        if mx<max(i):
            mx = max(i)
    print(mx-1)
