from sys import stdin, stdout

input = stdin.readline 

n = int(input())

for i in range(n):
    number = int(input())
    array = [list(map(int,input().split()))for _ in range(2)]

    for j in range(1,number):
        if j==1:
            array[0][j] += array[1][j-1]
            array[1][j] += array[0][j-1]
        else:
            array[0][j] += max(array[1][j-1],array[1][j-2])
            array[1][j] += max(array[0][j-1],array[0][j-2])

    print(max(array[0][number-1],array[1][number-1]))

