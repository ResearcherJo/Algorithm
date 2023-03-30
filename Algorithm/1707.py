import sys
from collections import deque

input = sys.stdin.readline

def bfs(array, n, visit, group):
    queue = deque([n])
    visit[n] = group

    while queue:
        x = queue.popleft()

        for i in array[x]:
            if not visit[i]:
                queue.append(i)  # 그 정점들을 추가하고
                visit[i] = -1 * visit[x]
            elif visit[x] == visit[i]:
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