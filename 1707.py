import sys
from collections import deque

input = sys.stdin.readline

#bfs를 이용한 그래프 탐색
def bfs(array, n, visit, group):
    queue = deque([n]) # 방문할 곳(n)을 queue에 넣는다.

    visit[n] = group # 방문할 곳을 group(1)으로 표시한다.

    while queue:
        x = queue.popleft()

        for i in array[x]:
            if not visit[i]: #방문할 곳과 연결된 노드가 방문하지 않았다면
                queue.append(i)  # 그 노드을 추가하고
                visit[i] = -1 * visit[x] #노드를 다른 그룹에 넣는다.
            elif visit[x] == visit[i]: # 연결된 노드와 같은 그룹이라면 이분그래프가 아닌 것이다.
                return False
            
    return True

k = int(input())

for i in range(k):
    v, e = map(int,input().split())
    array = [[] for i in range(v+1)]
    visit = [0] * (v+1)

    for j in range(e):
        u, v = map(int,input().split())
        array[u].append(v)
        array[v].append(u)

    for j in range(1, v+1):
        if not visit[j]:
            result = bfs(array, j, visit, 1)
        if not result:
            break
    
    print('YES'if result else 'NO')