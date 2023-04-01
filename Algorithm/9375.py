from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = dict()
    for i in range(n):
        c, ty = input().split()
        if ty in dic:
            dic[ty] += 1
        else:
            dic[ty] = 2
    #print(dic)
    sum =1
    for j in dic:
        sum *= dic[j]

    print(sum-1)

