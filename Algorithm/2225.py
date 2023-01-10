from sys import stdin, stdout

input = stdin.readline 

number, n = map(int,input().split())

array = [[0]*(n+1) for i in range(number+1)]

array[0][0] = 1

for i in range(0, number+1):
    for j in range(1, n+1):
            array[i][j] = array[i-1][j] + array[i][j-1]

print(array)

print(array[number][n] % 1000000000)
