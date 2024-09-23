from sys import stdin

input = stdin.readline

goal = int(input()) #목표 채널

n = int(input()) #부서진 버튼 개수

#부서진 버튼이 없다면 입력을 받지 않는다.
if n>0:
    broken = list(map(str,input().split()))
else:
    broken = list()

#목표 채널이 100이라면 0을 출력하고 끝낸다.
if goal == 100:
    print(0)
else:
    #처음 초기값을 100에서 +-만 이용해서 목표채널로 가는 횟수로 초기화
    min_count = abs(100-goal)

    #0~1000000 까지의 모든 수를 돌아보면서 가능한 수 중에서 최소값을 갱신한다.
    #10000000인 이유는 목표 채널에 대해 아래에서 위로 올라가는 경우와 
    #위에서 아래로 내려가는 경우를 고려하기 위해서이다.
    for num in range(1000001):
        #num을 바로 입력할 수 있는지 확인
        for i in str(num):
            if i in broken:
                break
        #num을 바로 입력할 수 있다면
        else:
            #최소값 갱신 num으로 가서 +-를 눌러야하는 횟수를 더하는것
            min_count = min(min_count,len(str(num))+abs(num-int(goal)))

    #최소값 출력
    print(min_count)
