from sys import stdin, stdout

input = stdin.readline 


array = [[0 for i in range(2)] for j in range(100)]

array[1][1] = 1

n = int(input())

for i in range(2,n+1):
    for j in range(2):
        array[i][0] = array[i-1][0]+array[i-1][1]
        array[i][1] = array[i-1][0]

print(sum(array[n][0:2]))

