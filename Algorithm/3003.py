from sys import stdin, stdout

input = stdin.readline


an = [1,1,2,2,2,8]

n = list(map(int, input().split()))

for i in range(len(an)):
    print(an[i]-n[i], end=" ")