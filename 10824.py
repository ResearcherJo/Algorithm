from sys import stdin

input = stdin.readline

array = list(input().split())

a = int(array[0]+array[1])
b = int(array[2]+array[3])

print(a+b)