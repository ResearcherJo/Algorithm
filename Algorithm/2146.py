from sys import stdin
from collections import deque

input = stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

queue = deque()

def init(array, n):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                queue.append([i,j])

def bfs(array,n):
    while queue:
        now = queue.popleft()

        for i in range(4):
            x = now[1] + dx[i]
            y = now[0] + dy[i]
            if x>=0 and x<n and y>=0 and y<n:
                if array[y][x] == 0:
                    array[y][x] = array[now[0]][now[1]] + 1
                    queue.append([y,x])


n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

init(array,n)
bfs(array,n)

res = 999

for i in range(n):
    print(*array[i])
