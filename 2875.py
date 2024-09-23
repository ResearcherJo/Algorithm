'''
풀이
https://velog.io/@babnbabn/2875번-대회or인턴-Python
'''
from sys import stdin

input = stdin.readline

n, m, k = map(int,input().split())

boy_team = n//2
girl_team = m
team = 0

#만들 수 있는 팀의 수를 team에 저장한다.
if boy_team>=girl_team:
    team = girl_team
else:
    team = boy_team

#팀이 될 수 없는 인원들은 인턴쉽을 보낸다.
n = n-(team*2)
m = m-team
k = k - n - m

#남은 인원들로 인턴쉽 인원이 된다면 team을 출력한다.
if k<=0:
    print(team)
#남은 인원들로 인턴쉽 인원이 부족하다면 만들어진 팀에서 인원을 충당한다.
else:
    if k%3==0:
        team = team - (k//3)
    else:
        team = team - ((k//3)+1)
    print(team)