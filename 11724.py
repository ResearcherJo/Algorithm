import sys 
sys.setrecursionlimit(10**6) #제귀 깊이 변경

input = sys.stdin.readline

#dfs
def dfs(array, n, visit):
    if visit[n]!=0:
        return
    
    visit[n] = 1

    for i in range(len(array[n])):
        if array[n][i] == 1:
            dfs(array, i, visit)
        

n, m = map(int,input().split())
array = [[0 for j in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]
count = 0

for i in range(m):
    x, y = map(int,input().split())
    array[x][y] = array[y][x] = array[x][x] = array[y][y] = 1

#dfs로 방문 안한 곳들은 연결되어 있는 노드까지 한번 돌기
for i in range(1, n+1):
    if visit[i] == 0:
        dfs(array,i,visit)
        count+=1

print(count)



    
