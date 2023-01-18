'''
    상하좌우
    
    여행가 A는 NxN 크기의 정사각형 공간에 서 있고, 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
    가장 왼쪽 위 좌표는 (1, 1)이고 가장 오른쪽 아래 좌표는 (N, N)이다.
    상하좌우로 이동할 수 있으며, 시작 좌표는 (1,1)이다.
    계획서대로 이동하면 되는데
    L, R, U, D는 각각 왼쪽, 오른쪽, 위, 아래로 한칸씩 이동하라는 뜻이다.
    만약 공간을 벗어나는 움직임이 있다면 그 움직임은 무시하고 다음으로 넘어간다.

'''

n = int(input())

now = [1,1]
dic = {'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}

T = list(input().split())

for i in T:
    if now[0]+dic[i][0]>=1 and now[1]+dic[i][1]>=1 and now[0]+dic[i][0]<=n and now[1]+dic[i][1]<=n:
        now[0]+=dic[i][0]
        now[1]+=dic[i][1]
print(now[0],now[1])

'''
    # N 입력받기
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    
    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    
    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
    
    print(x, y)
'''