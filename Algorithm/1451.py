from sys import stdin

input = stdin.readline

n, m = map(int,input().split())
array = [list(map(int,list(input().strip()))) for _ in range(n)]
ma = 0

def getSum(startx, starty, endx, endy):
    sum = 0
    for i in range(starty,endy+1):
        for j in range(startx,endx+1):
            sum+=array[i][j]
    return sum

#1번 모양
for i in range(n-2): #n-2인 이유는 나눌 곳을 최소 2만큼 만들어 둬야하기 때문이다.
    for j in range(i+1,n-1): #n-1인 이유는 나눌 곳을 최소 1만큼 만들어 둬야하기 때문이다.
        r1 = getSum(0,0,m-1,i) #1-1
        r2 = getSum(0,i+1,m-1,j) #1-2
        r3 = getSum(0,j+1,m-1,n-1) #1-3
        ma = max(ma,r1*r2*r3)

#2번 모양
for i in range(m-2): 
    for j in range(i+1,m-1):
        r1 = getSum(0,0,i,n-1) #2-1
        r2 = getSum(i+1,0,j,n-1) #2-2
        r3 = getSum(j+1,0,m-1,n-1) #2-3
        ma = max(ma,r1*r2*r3)

#3번 모양
for i in range(m-1,0,-1):
    for j in range(n-1):
        r1 = getSum(0,0,i,j) #3-1
        r2 = getSum(0,j+1,i,n-1) #3-2
        r3 = getSum(i+1,0,m-1,n-1) #3-3
        ma = max(ma,r1*r2*r3)

#4번 모양
for i in range(m-1):
    for j in range(n-1):
        r1 = getSum(0,0,i,n-1) #4-1
        r2 = getSum(i+1,0,m-1,j) #4-2
        r3 = getSum(i+1,j+1,m-1,n-1) #4-3
        ma = max(ma,r1*r2*r3)

#5번 모양
for i in range(n-1):
    for j in range(m-1):
        r1 = getSum(0,0,m-1,i) #5-1
        r2 = getSum(0,i+1,j,n-1) #5-2
        r3 = getSum(j+1,i+1,m-1,n-1) #5-3
        ma = max(ma,r1*r2*r3)

#6번 모양
for i in range(n-1,0,-1):
    for j in range(m-1):
        r1 = getSum(0,0,j,i) #6-1
        r2 = getSum(j+1,0,m-1,i) #6-2
        r3 = getSum(0,i+1,m-1,n-1) #6-3
        ma = max(ma,r1*r2*r3)

print(ma)