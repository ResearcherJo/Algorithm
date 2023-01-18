


n = int(input())

nl = list(map(int,input().split()))

nl.sort()

for i in range(1,n):
    nl[i] = nl[i]+nl[i-1]

print(sum(nl))