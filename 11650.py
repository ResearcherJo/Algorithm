from sys import stdin

input = stdin.readline

n = int(input())

array = [list(map(int,input().split())) for i in range(n)]

array.sort(key=lambda x : x[1])
array.sort(key=lambda x : x[0])

for i in range(n):
    print(array[i][0],array[i][1])