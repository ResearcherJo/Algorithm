from sys import stdin

input = stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]
dp = [0 for i in range(n)]

dp[0] = array[0]

for i in range(1, n):
    if i==1:
        dp[1] = array[1]+array[0]
    elif i==2:
        dp[2] = max(array[2]+dp[0],array[2]+array[1])
    else:
        dp[i] = max(dp[i-2]+array[i], array[i]+array[i-1]+dp[i-3])

print(dp[-1])