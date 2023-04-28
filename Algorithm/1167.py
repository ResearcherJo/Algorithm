import sys 

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n, memo):
    global m
    m = max(m, memo)
    visit[n]=1
    
    for i in array[n]:
        if visit[i[0]]==0:
            #print('node : {}'.format(i[0]))
            #print('memo : {}'.format(memo))
            dfs(i[0],memo+i[1])
            
                
            





n = int(input())
array = [[] for _ in range(n+1)]
visit = [0] * (n+1)
m = 0

for i in range(n):
    li = list(map(int,input().split()))

    for j in range(1,len(li)-1,2):
        array[li[0]].append((li[j],li[j+1]))

for i in range(1,n+1):    
    visit = [0] * (n+1)
    dfs(i,0)

print(m)

'''
for i in array:
    print(*i)
'''


