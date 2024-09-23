'''
풀이
https://velog.io/@babnbabn/12015번-가장-긴-증가하는-부분-수열-2-Python
'''
import bisect
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]

for i in range(n):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])#arr[i]가 들어갈 곳을 반환
        dp[idx] = arr[i]#dp의 값과 arr[i]를 교환

print(len(dp))
