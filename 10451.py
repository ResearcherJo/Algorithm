from sys import stdin

input = stdin.readline

def DFS(array, v, visit):
    if visit[v]!=0: #방문 한적이 있으면 돌아간다.
        return 
    visit[v] = 1

    for i in range(len(array[v])):#가장 가까운 것 부터 계속 들어가면서 방문한다.
        if array[v][i]==1: 
            DFS(array, i,visit)



t = int(input())

for i in range(t):
    n = int(input())
    array = [i for i in range(1,n+1)] #1 ~ n까지의 수가 들어있는 배열
    array_temp = list(map(int,input().split()))
    visit = [0 for i in range(n+1)]
    count = 0

    matrix = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n): #1~n이 가리키게 행렬을 만든다.
        matrix[array[i]][array_temp[i]] = 1

    for i in range(1,n+1):
        if visit[i] != 1:
            DFS(matrix,i,visit)
            count += 1

    print(count)