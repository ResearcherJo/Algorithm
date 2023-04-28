'''
풀이
https://velog.io/@babnbabn/2146번-다리-만들기-Python
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
k = 2
m =  sys.maxsize

dx = [0,1,0,-1]
dy = [1,0,-1,0]

#섬을 구분하는 함수, k로 섬을 바꿔준다.
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

#다리를 놓는 함수 최소값 m을 계속해서 최신화 한다.
def bfs(k):
    global m
    queue = deque()
    dist = [[-1]*n for _ in range(n)]

    #k번째 섬을 기준으로 하기 위한 코드, 
    for i in range(n):
        for j in range(n):
            if array[i][j] == k:
                queue.append([i,j])
                #섬에서 시작하기 위해 섬을 0으로 바꿔놓는다.
                dist[i][j] = 0


    while queue:
        now = queue.popleft()

        for i in range(4):
            x = now[1] + dx[i]
            y = now[0] + dy[i]
            if x>=0 and x<n and y>=0 and y<n:
                #다음이 k번 섬이 아닌 다른 섬이라면 다리가 놓여 진 것이다.
                #가장 먼저 만들어진 다리가 가장 짧은 다리이다. 그렇기 때문에, 다리가 만들어지자 마자 m이랑 비교하면 된다.
                if array[y][x]!=k and array[y][x] > 0:
                    #그 다리가 최소값이라면 m을 바꾼다.
                    m = min(dist[now[0]][now[1]],m)
                    return
                #바다이고, 다리를 놓은 적이 없는 곳이라면 다리를 놓는다.
                elif array[y][x] == 0 and dist[y][x] == -1:
                    dist[y][x] = dist[now[0]][now[1]] + 1

                    queue.append([y,x])
    

#섬을 마크하기
for i in range(n):
    for j in range(n):
        if array[i][j] == 1 :
            init(j,i,k)
            k+=1

#다리를 놓기
for i in range(2,k):
    bfs(i)

print(m)


