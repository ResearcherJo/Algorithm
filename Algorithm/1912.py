from sys import stdin

input = stdin.readline

n = int(input())

array = list(map(int,input().split()))

dp = [0 for i in range(n)]

dp[0] = array[0]

for i in range(1,n) :
    if(dp[i-1]>=0):
        dp[i] = array[i]+dp[i-1] 
    else:
        dp[i] = array[i]

print(max(dp))