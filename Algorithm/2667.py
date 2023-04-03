from sys import stdin

input = stdin.readline

#상하좌우순으로 검색하기 위해서 만든 거
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(array, i,j,n):
    global count
    if array[i][j] != '1':
        return

    array[i][j] = '-1' #방문 했음을 알리는 것
    count +=1#방문한 단지내 집을 카운트

    #상하좌우 순으로 보면서 탐색
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x<n and x>=0 and y<n and y>=0: #배열 끝을 넘지 않게
            if array[x][y] == '1':
                dfs(array, x,y,n)


n = int(input())

array = [list(input()) for _ in range(n)]
c = [0] + list()

for i in range(n):
    for j in range(n):
        if array[i][j] == '1':
            count = 0
            dfs(array,i,j,n)
            c.append(count) #단지내 집을 저장
            c[0] += 1 # 단지 수를 1 더함

c[1:] = sorted(c[1:]) #단지내 집을 오름차순으로 정렬

for i in c:
    print(i)

'''
print(*c) #단지, 단지내 집수

#탐색을 다 했는지 확인하는 소스
for i in range(n):
    for j in range(n):
        print('{0:3}'.format(array[i][j]),end='')
    print()
'''