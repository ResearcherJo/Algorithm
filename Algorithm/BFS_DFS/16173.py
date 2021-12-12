

import sys
sys.setrecursionlimit(10**6)
l = list()

Bol = True

n = int(sys.stdin.readline())

for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))

visit = [[False]*n for i in range(n)]


def dfs(x,y,visit):
    
    if x==n-1 and y==n-1:
        global Bol
        Bol = False
        return     
    if x<0 or y<0 or x>=n or y>=n:
        return
    if visit[x][y]:
        return
    visit[x][y]=True    
    dfs(x+l[x][y],y,visit)
    dfs(x,y+l[x][y],visit)
    

dfs(0,0,visit)

if Bol:
    print('Hing')
else:
    print('HaruHaru')
    

    
    
'''
    DFS할때 visit으로 방문했는지 확인을 해주면 메모리를 아낄 수 있다.
'''