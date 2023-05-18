from sys import stdin

input = stdin.readline

#start : 처음 시작한 노드, node : 현재 노드, cnt : 방문한 노드 개수, m : 지금가지의 비용
def dfs(start,node, cnt, m):

    global sum

    #방문하지 않은 노드가 1개 남았을때 다시 start로 돌아 갈 수 있다면 sum을 최신화 시켜준다.
    if cnt == n-1 and arr[node][start]!=0:
        sum = min(sum,m+arr[node][start])
        return

    #중간에 sum보다 m이 넘어가면 이미 그른것이다.
    if m>sum:
        return

    visited[node] = 1
    
    for i in range(n):
        #i노드를 갈 수 있고, 방문하지 않았다면 방문
        if arr[node][i]!=0 and not visited[i]: 
                dfs(start,i,cnt+1,m+arr[node][i])
                visited[i] = 0 #방문이 끝났다면 다시 방문할 수 있게 초기화해준다.


sum = int(1e9) #최대값을 넣어준다.
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

#모든 노드에서 시작해서 최소비용을 구한다.
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i,i,0,0)
    
print(sum)
