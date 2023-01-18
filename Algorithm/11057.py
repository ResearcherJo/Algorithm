from sys import stdin, stdout

input = stdin.readline 

array = [[0 for j in range(10)] for i in range(10001)]

n = int(input())

for i in range(10):
    array[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        array[i][j] = sum(array[i-1][0:j+1])

print(sum(array[n][0:10])%10007)