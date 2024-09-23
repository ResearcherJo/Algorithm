from sys import stdin, stdout

input = stdin.readline 

INF = int(1e9)

n, m = map(int,input().split())

# INIT / graph를 초기와한다.
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

# 서로 연결되있는 노드끼리를 1로 바꾼다.
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

min = INF # 최소 베이컨 수를 저장하는 함수
index = -1 # 최소 베이컨 수를 가지는 노드를 저장

for i in range(1,n+1):
    s = sum(graph[i][1:])
    if min > s:
        min = s
        index = i

print(index)

