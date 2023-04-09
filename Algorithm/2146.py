import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
k = 2
m =  sys.maxsize

dx = [0,1,0,-1]
dy = [1,0,-1,0]

#섬을 구분하는 함수 k로 섬을 바꿔준다.
def init(x, y, k):
    queue = deque()
    queue.append([y,x])

    array[y][x] = k

    while queue:
        now = queue.popleft()
        for i in range(4):
            x = now[1] + dx[i]
            y = now[0] + dy[i]
            if x>=0 and x<n and y>=0 and y<n:
                if array[y][x] == 1:
                    array[y][x] = k
                    queue.append([y,x])

def bfs(k):
    global m
    queue = deque()
    dist = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if array[i][j] == k:
                queue.append([i,j])
                dist[i][j] = 0

    while queue:
        now = queue.popleft()

        for i in range(4):
            x = now[1] + dx[i]
            y = now[0] + dy[i]
            if x>=0 and x<n and y>=0 and y<n:
                if array[y][x]!=k and array[y][x] > 0:
                    m = min(dist[now[0]][now[1]],m)
                    return
                elif array[y][x] == 0 and dist[y][x]==-1:
                    dist[y][x] = dist[now[0]][now[1]] + 1

                    queue.append([y,x])
    




#섬을 마크하기
for i in range(n):
    for j in range(n):
        if array[i][j] == 1 :
            init(j,i,k)
            k+=1

'''
print('array')
for i in array:
    print(*i)
'''

for i in range(2,k):
    bfs(i)

print(m)


