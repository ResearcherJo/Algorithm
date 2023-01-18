


def dfs(a):
    if dp[a]==1:
        return
    dp[a]=1
    for i in range(n+1):
        if l[a][i]==1:
            dfs(i)
        


n = int(input())
t = int(input())

l = [[0]*(n+1) for _ in range(n+1)]
dp = [0 for _ in range(n+1)]


for i in range(t):
    x, y = map(int,input().split())    
    l[x][y] = l[y][x] = 1
    
dfs(1)

print(sum(dp)-1)
    
    