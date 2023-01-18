from sys import stdin

input = stdin.readline

n = int(input())

array = list(map(int,input().split()))
re_array = array[::-1]

dp = [1 for i in range(n)]
re_dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[j]+1,dp[i])
        if re_array[i] > re_array[j]:
            re_dp[i] = max(re_dp[j]+1,re_dp[i])

re_dp = re_dp[::-1]
#처음에 re_array로 뒤집어서 구했으니 다시 뒤집어준다.

for i in range(n):
    dp[i] = dp[i]+re_dp[i]-1
    #1을 빼는 이유는 i번째 수가 중복되어서 계산되었기 때문이다.

print(max(dp))