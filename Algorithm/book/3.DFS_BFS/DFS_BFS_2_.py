'''
    
    미로 탈출
    
    동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혀 있는 상황이다. 미로에는 여러 마리의 괴물이 이를 피해 탈출해야 하는 상황. 
    동빈이는 (1,1) 위치에 있고 미로의 탈출구는 (N,M)의 위치에 존재하며 한번에 한칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0이다. 괴물이 없는 부분은 1로 표시한다.
    미로는 반드시 탈출 가능한 형식으로 주어지고. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소의 칸 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 카운트 합니다.

    1.1. 예시 1Permalink
    예시로 아래와 같은 미로판의 경우를 보자.
    5 6
    101010
    111111
    000001
    111111
    111111
    첫 행 첫 열에서 부터 시작해서 끝행 끝열에서 탈출하므로 10을 출력하면 된다.

    1.2. 입력 조건Permalink
        첫 번째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 다음 N 개의 줄에는 각각 M 개의 정수 (0 or 1)로 미로의 정보가 주어진다. 
        각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
        
    1.3. 출력 조건Permalink
        첫째 줄에 최소 이동 칸의 개수를 출력한다.

'''


from collections import deque
# 상하좌우 살펴보고 1이면 해당칸으로 이동, 그리고 result +1 하는 방식사용
#입력 받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 1. 상하좌우 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def bfs(x,y):

    q = deque()
    q.append((x,y)) # 0,0 큐에 넣고 시작
    
    while q: # 큐가 빌때까지
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 범위를 벗어나면 무시하고 다음 i로
            if nx >= n or ny >= m or nx < 0 or ny < 0 or graph[nx][ny] == 0:
                continue

            # nx, ny 노드가 괴물칸 (0) 인 경우도 다음 i로
            #if graph[nx][ny] == 0:
             #   continue
            
            # 갈 수 있는 길인 1이면
            if graph[nx][ny] == 1
            
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))
