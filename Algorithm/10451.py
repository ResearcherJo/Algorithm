from sys import stdin
#from collections import deque

input = stdin.readline

def DFS(array, v, visit):
    if visit[v]!=0: #방문 한적이 있으면 돌아간다.
        return 
    visit[v] = 1
    #print(v,end=' ')
    for i in range(len(array[v])):#가장 가까운 것 부터 계속 들어가면서 방문한다.
        if array[v][i]==1: 
            DFS(array, i,visit)



t = int(input())

for i in range(t):
    n = int(input())
    array = [i for i in range(1,n+1)]
    array_temp = list(map(int,input().split()))
    visit = [0 for i in range(n+1)]
    count = 0

    matrix = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n):
        matrix[array[i]][array_temp[i]] = 1

    for i in range(1,n+1):
        if visit[i] != 1:
            DFS(matrix,i,visit)
            count += 1

    print(count)