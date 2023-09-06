from sys import stdin, stdout

input = stdin.readline 

t = int(input())

for _ in range(t):
    m, n, x, y = map(int,input().split())
    count = x # x를 맞추고 시작

    while count <= m*n:        
        if (count-x)%m==0 and (count-y)%n==0: # x, y가 둘다 맞다면
            print(count)
            break
        count += m
    else:
        print(-1)