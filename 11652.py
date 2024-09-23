from sys import stdin

input = stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

cnt = 1
idx = 0
max = 0

array.sort()

for i in range(1,len(array)):
    if array[i-1] == array[i]:
        cnt+=1
    else:
        if cnt>max:
            max = cnt
            idx = i-1
        cnt =1

if cnt>max:
    max = cnt
    idx = n-1

print(array[idx])

