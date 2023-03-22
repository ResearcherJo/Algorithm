from sys import stdin
from collections import deque

input = stdin.readline

#깊이 우선 탐색
def DFS(array, v, visit):
    if visit[v]!=0: #방문 한적이 있으면 돌아간다.
        return 
    visit[v] = 1
    print(v,end=' ')
    for i in range(len(array[v])):#가장 가까운 것 부터 계속 들어가면서 방문한다.
        if array[v][i]==1: 
            DFS(array, i,visit)

#넓이 우선 탐색
def BFS(array, v, visit):
    queue = deque([v])
    visit[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(len(array[v])): #처음 방문한 노드를 큐에 넣고, 앞에서 부터 빼면서 다음 방문할 것을 큐에 넣는다.
            if array[v][i] == 1 and visit[i]==False:
                queue.append(i)
                visit[i] = True



n, m, v = map(int,input().split())
array = [[0 for j in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m): #노드끼리 연결되어 있는 것을 표시한다.
    x, y = map(int,input().split())
    array[x][y] = array[y][x]= array[x][x] = array[y][y] = 1

DFS(array,v,visit)
visit = [True]+[False for i in range(n)]
print()
BFS(array,v,visit)
