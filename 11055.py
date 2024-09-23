from sys import stdin, stdout

input = stdin.readline 

n = int(input())

array = list(map(int,input().split()))

dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = array[i]
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(array[i]+dp[j],dp[i])
            #array[i]+dp[j] 와 dp[i]를 비교하는 이유는 전의 숫자를 더한다고 무조건 최대 합이 나오는게 아니기 때문이다.

print(max(dp))

