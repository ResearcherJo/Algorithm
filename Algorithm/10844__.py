from sys import stdin, stdout

input = stdin.readline 

array = [[0 for i in range(11)] for j in range(101)]

n = int(input())

for i in range(1,10):
    array[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j==0:
            array[i][j] = array[i-1][j+1]
        elif j==9:
            array[i][j] = array[i-1][j-1]
        else:
            array[i][j] = array[i-1][j-1] + array[i-1][j+1]

print(sum(array[n][0:10])%1000000000)

