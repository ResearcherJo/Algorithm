'''
    음료수 얼려 먹기 
    
    N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
    구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
    이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
    다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개가 생성된다

    입력
    첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
    두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
    이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
    
    출력
    한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
'''

import sys

n=0
m=0
count=0
def dfs(stack,x,y,visited):
    
    if visited[x][y]:
        return
    
    visited[x][y]=True
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(stack,i,j,visited)
                
    
    


n, m = map(int,input().split())
ma = list()

visited = [[False]*m for i in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    
    ma.append(list(line))
    
for i in range(n):
    for j in range(m):
        if ma[i][j]=='1':
            visited[i][j]=True
print(visited)            
dfs(ma,0,0,visited)
print(visited)   

        
print(ma)

'''
    아이디어는 냈으나 어떻게 구현할지가 정말 몰랐고, 생각해낸 구현 방법도 틀렸다. 문제에 답이 있었지만 제대로 안 읽었다.
    
    # N, M을 공백을 기준으로 구분하여 입력 받기
    n, m = map(int, input().split())
    
    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    
    # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            # 해당 노드 방문 처리
            graph[x][y] = 1
            # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False
    
    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1

    print(result) # 정답 출력
'''
    
    