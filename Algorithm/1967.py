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

for i in range(n-1):
    p, c, e = map(int,input().split())
    #방향이 없는 트리를 만들기 위해 p->c 와 c->p 둘다 만든다.
    array[p].append((c,e))
    array[c].append((p,e))
    
dfs(1,0)


v = visit.index(max(visit)) #node(1)에서 가장 먼 노드 v

visit = [-1] * (n+1)
dfs(v,0) #node(v)에서 가장 먼 node까지의 길이를 다시 구한다.

print(max(visit))