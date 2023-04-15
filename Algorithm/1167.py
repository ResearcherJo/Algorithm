'''
풀이
https://velog.io/@babnbabn/1167번-트리의-지름-Python
'''
import sys 

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n, m):
    visit[n] = m #visit에 n까지의 거리를 저장한다.
    
    for i in array[n]:
        if visit[i[0]]==-1: #i[0]를 방문하지 않았다면 방문
            dfs(i[0],m+i[1]) #i[0]을 방문하면서 거리를 n에서 i[0]까지의 거리를 더한다.


n = int(input())
array = [[] for _ in range(n+1)]
visit = [-1] * (n+1)

for i in range(n):
    li = list(map(int,input().split()))

    for j in range(1,len(li)-1,2):
        array[li[0]].append((li[j],li[j+1]))
    
dfs(1,0)


v = visit.index(max(visit)) #node(1)에서 가장 먼 노드 v

visit = [-1] * (n+1)
dfs(v,0) #node(v)에서 가장 먼 node까지의 길이를 다시 구한다.

print(max(visit))

