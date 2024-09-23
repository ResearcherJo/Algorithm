from sys import stdin

input = stdin.readline

r, c = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(r)]

if r%2!=0:
    str = 'R'*(c-1) + ('D' + 'L'*(c-1) + 'D' + 'R'*(c-1))*(r//2)
    print(str)
elif c%2!=0:
    str = 'D'*(r-1) + ('R' + 'U'*(r-1) + 'R' + 'D'*(r-1)) *(c//2)
    print(str)
else: 
    lowest = 1001  # 가장 작은 값을 찾기위해 설정 기쁨점수는 1000보다 작은 양의 정수이다.
    lowPosition = [-1, -1]  # 가장 작은 값의 위치
   
    #최소값과 위치 찾기
    for i in range(r):
        if i % 2 == 0:  # 짝수 행 이면 홀수칸만 본다.
            for j in range(1, c, 2):
                if lowest > arr[i][j]:
                    lowest = arr[i][j]
                    lowPosition = [i, j]
        else:  # 홀수 행 이면 짝수칸만 본다.
            for k in range(0, c, 2):
                if lowest > arr[i][k]:
                    lowest = arr[i][k]
                    lowPosition = [i, k]

    #피해갈 위치의 좌측최상단까지 간다.
    result = ("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (lowPosition[1] // 2)

    x = 2 * (lowPosition[1] // 2) # 홀수를 짝수로 만들어준다. , 시작점은 항상 짝수여야 하기때문이다.
    y = 0

    xbound = 2 * (lowPosition[1] // 2) + 1 #시작점의 x보다 하나 큰 것이 bound가 된다.

    #삭제할 위치의 가장 아래 오른쪽까지 간다.
    while x != xbound or y != r - 1:
        #끝이 아니고, 피할 위치가 아니면 오른쪽으로 간다.
        if x < xbound and [y, xbound] != lowPosition:
            x += 1
            result += 'R'
        #끝이고, 피할 위치가 아니면 왼쪽으로 간다.
        elif x == xbound and [y, xbound - 1] != lowPosition:
            x -= 1
            result += 'L'
        #가장 아래쪽이 아니면 내려간다.
        if y != r - 1:
            y += 1
            result += 'D'

    #도착지점까지 간다.
    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - lowPosition[1] - 1) // 2)


    print(result)