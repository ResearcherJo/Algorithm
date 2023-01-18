from sys import stdin, stdout

input = stdin.readline


n = [list(map(int,input().split())) for _ in range(int(input()))]

n.sort(key = lambda x : x[0])
n.sort(key = lambda x : x[1])


count=0
key = -1

for i in n:
    if key<=i[0]:
        key = i[1]
        count+=1
        

print(count)