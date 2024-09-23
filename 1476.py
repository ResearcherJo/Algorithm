'''
from sys import stdin

input = stdin.readline

E, S, M = map(int,input().split())
e, s, m = 0, 0, 0
i = 0

while True:
    e = i%15+1 # 1~15
    s = i%28+1 # 1~28
    m = i%19+1 # 1~19
    #목표 연도라면
    if e == E and s == S and m == M:
        #i를 0부터 시작했기때문에 +1해준다.
        print(i+1)
        break
    i+=1
'''

from sys import stdin

input = stdin.readline

E, S, M = map(int,input().split())
year = 1

while True:
    #연도(year)에서 주어진 연도(E,S,M)를 뺏을 때의 나머지가 모두 0이라면 준규가 사는 나라의 연도가 될것이다.
    if (year-E)%15==0 and (year-S)%28 == 0 and (year-M)%19 == 0:
        break
    year+=1

print(year)

