from sys import stdin

input = stdin.readline

n, m = map(int,input().split())

#세로가 1인 경우
if n==1:
    print(1)
#세로가 2인경우
elif n==2:
    print(min((m+1)//2,4))
#가로가 7미만인 경우
elif m<7:
    print(min(4,m))
#그 외
else:
    print(m-7+5)