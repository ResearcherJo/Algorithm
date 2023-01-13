from sys import stdin

input = stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

array.sort()

for i in range(n):
    print(array[i])