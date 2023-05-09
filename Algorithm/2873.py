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
    lowest = 1001  # 가장 작은 값을 찾기위해 설정
    lowPosition = [-1, -1]  # 가장 작은 값의 위치
    for i in range(r):
        if i % 2 == 0:  # 1
            for j in range(1, c, 2):
                if lowest > arr[i][j]:
                    lowest = arr[i][j]
                    lowPosition = [i, j]
        else:  # 2
            for k in range(0, c, 2):
                if lowest > arr[i][k]:
                    lowest = arr[i][k]
                    lowPosition = [i, k]

    result = ("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (lowPosition[1] // 2)
    x = 2 * (lowPosition[1] // 2)
    y = 0
    xbound = 2 * (lowPosition[1] // 2) + 1
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != lowPosition:
            x += 1
            result += 'R'
        elif x == xbound and [y, xbound - 1] != lowPosition:
            x -= 1
            result += 'L'
        if y != r - 1:
            y += 1
            result += 'D'

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - lowPosition[1] - 1) // 2)
    #result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - lowPosition[1] - 1) // 2)

    print(result)