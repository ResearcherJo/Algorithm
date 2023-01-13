from sys import stdin

input = stdin.readline

n = int(input())

array = [list(input().split()) for i in range(n)]

for i in range(n):
    array[i][0] = int(array[i][0])

array.sort(key=lambda x : x[0])

for i in range(n):
    print(array[i][0], array[i][1])
