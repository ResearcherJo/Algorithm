import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)#RecursionError 방지

#8가지 방향을 탐색하기 위한 x, y값 변화
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def dfs(array, i,j, w, h):
    if array[i][j] != 1:
        return
    
    array[i][j] = -1

    for k in range(8): #8가지 방향을 탐색
        x = j + dx[k]
        y = i + dy[k]
        if x<w and x>=0 and y<h and y>=0: #지도 밖으로 나가지 않게 탐색
            if array[y][x] == 1:
                dfs(array,y,x,w,h)


while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break

    array = [list(map(int,input().split())) for _ in range(h)]


    count = 0
    for i in range(h):
        for j in range(w):
            if array[i][j] == 1:
                dfs(array,i,j,w,h)
                count +=1

    print(count)