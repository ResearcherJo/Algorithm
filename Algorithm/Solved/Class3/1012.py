import sys

sys.setrecursionlimit(10**6)
def dfs(x,y,visit,n,m):
    if x<0 or y<0 or y>=m or x>=n:
        return
    
    if visit[x][y]:
        visit[x][y] = False
        
        dfs(x+1,y,visit,n,m)
        dfs(x-1,y,visit,n,m)
        dfs(x,y+1,visit,n,m)
        dfs(x,y-1,visit,n,m)


def prin(list):
    for i in list:
        for j in i:
            print(j,end=' ')
        print()
        
        
T = int(input())

for i in range(T):
    m, n, k = map(int,sys.stdin.readline().split())
    count=0
    l = [[0]*m for i in range(n)]
    visit = [[False]*m for i in range(n)]
    
    for j in range(k):
        y, x = map(int,sys.stdin.readline().split())
        l[x][y] = 1
        visit[x][y] = True

    #prin(l)
    #print()
    for j in range(n):
        for v in range(m):
            if visit[j][v]:
                dfs(j,v,visit,n,m)
                #prin(l)
                #print()
                count+=1
                
    print(count)

'''
    2중 배열에서 어디가 x 고 어디가 y인지 중요하고 문제 잘 읽어 보자
''' 
    