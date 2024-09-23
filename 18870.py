

from sys import stdin

input = stdin.readline

dic = dict()

n = int(input())

num = list(map(int,input().split()))

nl = sorted(num)

count = 0
dic[nl[0]] = count

for i in range(1, len(nl)):
    if nl[i]!=nl[i-1]:
        count+=1
    dic[nl[i]] = count

for i in num:
    print(dic[i],end=' ')
