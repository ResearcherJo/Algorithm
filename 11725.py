from sys import stdin
from collections import deque

input = stdin.readline
queue = deque()

def bfs(graph, node, visit, parent):
    queue.append(node) #1을 넣고, 방문 표시 한다.
    visit[node] = 1

    while queue:
        nod = queue.popleft()
        
        for i in graph[nod]:#노드와 연결된 자식들 i
            if not visit[i]:#자식들 중에 방문 하지 않은 노드를 nod의 자식노드로 한다.
                queue.append(i)
                parent[i] = nod
                visit[i] = 1#i는 방문했음을 체크한다. 부모가 정해졌다는 의미이다.


n = int(input())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split()) #입력 받은 노드를 방향이 없게 graph에 넣는다.
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visit, parent)#노드 1부터 시작해서 각 노드의 부모노드를 찾는다.

for i in range(2,n+1):
    print(parent[i])


'''
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(node):
    visited[node] = 1 #node를 방문 표시 한다.
    for i in graph[node]: #node의 자식노드들을 i로 본다.
        if not visited[i]: #자식노드가 부모가 정해지지 않았다면 / 방향이 없기 때문에 누가 부모인지 정해지지 않았다.
            parent[i] = node #node가 i의 부모가 된다.
            dfs(i) #자식노드 한테 가서 똑같이 반복하낟.


n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split()) #입력 받은 노드를 방향이 없게 graph에 넣는다.
    graph[a].append(b)
    graph[b].append(a)

dfs(1)#노드 1부터 시작해서 각 노드의 부모노드를 찾는다.

for i in range(2,n+1):
    print(parent[i])
'''

