from sys import stdin
from collections import deque

input = stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()

#상자에 들어있는 토마토를 우선 다 queue에 넣는다.
def init(array):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if array[i][j][k] == 1:
                    queue.append([i,j,k])

#bfs를 이용해서 토마토를 계산한다.
def bfs(array):
    while queue:
        coordinate = queue.popleft()
        z = coordinate[0]
        y = coordinate[1]
        x = coordinate[2]

        #상하좌우를 살펴본다.
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + 0
            if next_x>=0 and next_x<m and next_y>=0 and next_y<n:
                if array[next_z][next_y][next_x] == 0:
                    #토마토가 있다면 +1한 값을 넣는다. 하루가 지났다는걸 의미한다.
                    array[next_z][next_y][next_x] = array[z][y][x] + 1
                    queue.append([next_z,next_y,next_x])

        #위, 아래를 살펴본다.  
        if next_z+1<h:
            if array[next_z+1][y][x] == 0:
                array[next_z+1][y][x] = array[z][y][x] + 1
                queue.append([next_z+1,y,x])
        if next_z-1>=0:
            if array[next_z-1][y][x] == 0:
                array[next_z-1][y][x] = array[z][y][x] + 1
                queue.append([next_z-1,y,x])
            

m, n, h = map(int,input().split())

array = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

init(array)

bfs(array)

boo = False
#상자에 안 익은 토마토가 있는지 체크하고, 있다면 -1을 출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] == 0:
                boo = True
                break
        if boo:
            break
    if boo:
        break

#안 익은 토마토가 있다면 -1
if boo:
    print('-1')
#안 익은 토마토가 없다면 가장 마지막에 익은 토마토를 찾는다.
else:
    m = 0
    for i in range(h):
        for j in range(n):
            m = max(m,max(array[i][j]))
    #1부터 시작해서 +1 했기 때문에 -1을 해준다.
    print(m-1)
        