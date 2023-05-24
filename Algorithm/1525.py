from sys import stdin
from collections import deque

#입력값을 한줄 문자열로 입력받아서 puzzle에 넣는다.
puzzle = ""
for i in range(3):
    puzzle += "".join(list(input().split()))


visited = {puzzle:0} #전에 만들었던 모양이 아닌지 확인한다. key는 모양이고, value는 변경 횟수이다.
#비어있는 곳에서 상하좌우로 바꿀 변수다.
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#bfs에서 사용할 queue이다.
queue = deque()
queue.append(puzzle)

def bfs():
    

    while queue:
        puzzle = queue.popleft()
        cnt = visited[puzzle] #puzzle모양이 만들어진 횟수를 저장한다.
        z = puzzle.index('0') #비어있는 공간의 index를 z에 넣는다.

        #목표에 도착하면 cnt(횟수)를 반환한다.
        if puzzle=='123456780':
            return cnt

        #문자열형태인(한줄로 된)상태에서 비어있는 곳의 x,y값을 뽑아낸다.
        x = z//3
        y = z%3

        for i in range(4):
            #빈 곳이 갈 수 있는 x, y좌표를 저장한다.
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 체크한다.
            if 0 <= nx<=2 and 0<= ny<=2:
                #다시 1차원 index로 변형하고, 값을 바꾼다.
                nz = nx*3 + ny
                puzzle_list = list(puzzle)
                puzzle_list[nz], puzzle_list[z] = puzzle_list[z], puzzle_list[nz]
                new_puzzle = "".join(puzzle_list)

                #만약 바꾼 값이 전에 만들었던 모양이 아니라면 저장한다.
                if visited.get(new_puzzle,0)==0:
                    visited[new_puzzle] = cnt+1
                    queue.append(new_puzzle)
    #만들 수 없다면 -1을 리턴한다.
    return -1

print(bfs())