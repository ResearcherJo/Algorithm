'''
풀이
https://velog.io/@babnbabn/2178번-미로-탐색
'''
from sys import stdin
from collections import deque

input = stdin.readline

#이동경로 (상,우,하,좌)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(array, n, m):
    queue = deque([])

    queue.append([0,0])#시작지점을 넣고 시작

    while queue:
        now = queue.popleft()

        for i in range(4):
            x = now[1] + dx[i]
            y = now[0] + dy[i]
            if x>=0 and x<m and y>=0 and y<n:#미로를 벗어나지 않는다면
                if array[y][x] == 1:#갈 수 있다면
                    array[y][x] = array[now[0]][now[1]] + 1 #1칸 지날때는 전칸의 횟수에 +1 하면 된다.
                    queue.append([y,x])
                    if x == m and y == n:
                        return True
                
    return False


n, m = map(int,input().split())
array = [list(map(int,input().strip())) for _ in range(n)]

bfs(array,n,m)
print(array[n-1][m-1])
