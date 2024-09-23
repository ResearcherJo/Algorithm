from sys import stdin

input = stdin.readline

S = input().strip()

array = [0 for i in range(26)]

for i in S:
    n = ord(i)-97
    array[n] +=1

print(*array)